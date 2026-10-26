"""Rebuild the unsplit CSV from frozen source snapshots and reviewed labels."""
import csv
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ReadableHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('p', 'div', 'li', 'br', 'tr', 'blockquote', 'h1', 'h2', 'h3'):
            self.parts.append('\n')
        if tag in ('td', 'th'):
            self.parts.append(' | ')
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'img':
            self.parts.append(f" [image: {attrs.get('alt', '')}; {attrs.get('src', '')}] ")
        if tag == 'iframe':
            self.parts.append(f" [embedded media: {attrs.get('src', '')}] ")

    def handle_endtag(self, tag):
        if tag == 'a' and self.links:
            url = self.links.pop()
            if url:
                self.parts.append(f' ({url})')
        if tag in ('p', 'div', 'li', 'tr', 'blockquote', 'h1', 'h2', 'h3'):
            self.parts.append('\n')

    def handle_data(self, data):
        self.parts.append(data)

    def text(self):
        return re.sub(r'\n\s*\n+', '\n\n', ''.join(self.parts)).strip()


def main():
    answers = []
    for page in (1, 2):
        answers.extend(json.loads((ROOT / f'data/source/sports-answers-page{page}.json').read_text()))
    annotations = json.loads((ROOT / 'data/source/annotations.json').read_text())
    rows, sources = [], []
    seen = set()
    for answer in answers:
        parser = ReadableHTML()
        parser.feed(answer['body'])
        text = parser.text()
        assert text and text not in seen, 'Empty or duplicate answer'
        seen.add(text)
        aid = str(answer['answer_id'])
        annotation = annotations[aid]
        rows.append({'text': text, 'label': annotation['label'], 'note': f"answer_id={aid}; {annotation['reason']}"})
        owner = answer.get('owner', {})
        sources.append({'answer_id': aid, 'question_id': answer['question_id'],
                        'url': f'https://sports.stackexchange.com/a/{aid}',
                        'author': owner.get('display_name', 'deleted user'),
                        'author_url': owner.get('link', ''),
                        'license': answer.get('content_license', ''),
                        'created_utc_epoch': answer['creation_date']})
    for path, data in [('labels.csv', rows), ('data/sources.csv', sources)]:
        with (ROOT / path).open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    from collections import Counter
    counts = Counter(row['label'] for row in rows)
    assert len(rows) >= 200
    assert max(counts.values()) / len(rows) <= .70, counts
    print(len(rows), dict(counts))

if __name__ == '__main__':
    main()
