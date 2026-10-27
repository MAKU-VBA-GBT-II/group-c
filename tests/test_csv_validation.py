"""Issue #25: bozuk CSV rapor üretilmeden reddedilmeli."""
import csv
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CsvValidationTests(unittest.TestCase):
    def run_analysis(self, field=None, value=None, status=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data').mkdir()
            (root / 'docs').mkdir()
            with (ROOT / 'data/banka-islemleri.csv').open(encoding='utf-8-sig', newline='') as f:
                reader = csv.DictReader(f)
                fields = reader.fieldnames
                rows = list(reader)
            if field:
                rows[0][field] = value
            if status:
                rows[0]['durum'] = status
            with (root / 'data/banka-islemleri.csv').open('w', encoding='utf-8-sig', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            report = root / 'docs/analiz-g1.md'
            report.write_text('existing report', encoding='utf-8')
            result = subprocess.run([sys.executable, str(ROOT / 'src/dq_analiz.py')],
                                    cwd=root, capture_output=True, text=True)
            return result, report.read_text(encoding='utf-8')

    def test_real_csv_succeeds(self):
        result, report = self.run_analysis()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('500', report)
        self.assertIn('17,837.13', report)
        self.assertIn('8,157,510.37', report)

    def test_invalid_values_preserve_report(self):
        cases = [('tarih', '2026-02-30'), ('tarih', '2026-1-1'),
                 ('tutar', 'abc'), ('tutar', 'NaN'),
                 ('islem_suresi_sn', '1.5'), ('musteri_id', 'abc'),
                 ('islem_turu', '')]
        for status in ('Başarılı', 'Başarısız', 'Beklemede'):
            for field, value in cases:
                with self.subTest(status=status, field=field, value=value):
                    result, report = self.run_analysis(field, value, status)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(field, result.stderr)
                    self.assertIn('2', result.stderr)
                    self.assertIn('data', result.stderr)
                    self.assertEqual(report, 'existing report')


if __name__ == '__main__':
    unittest.main()
