import json
import tempfile
import unittest
from pathlib import Path
from media_engine.rights import RightsError, validate_rights

class RightsValidationTests(unittest.TestCase):
    def write_manifest(self, root: str, tracks: list[dict]) -> Path:
        path = Path(root) / "rights.json"
        path.write_text(json.dumps({"tracks": tracks}), encoding="utf-8")
        return path

    def test_rejects_missing_track_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.write_manifest(tmp, [])
            with self.assertRaises(RightsError):
                validate_rights(manifest, "song.wav")

    def test_rejects_missing_derivative_permission(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.write_manifest(tmp, [{
                "file": "song.wav", "commercial_use": True,
                "derivative_works": False, "permission_evidence": "license-ref"
            }])
            with self.assertRaises(RightsError):
                validate_rights(manifest, "song.wav")

    def test_accepts_complete_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.write_manifest(tmp, [{
                "file": "song.wav", "commercial_use": True,
                "derivative_works": True, "permission_evidence": "license-ref"
            }])
            self.assertTrue(validate_rights(manifest, "song.wav")["commercial_use"])

if __name__ == "__main__":
    unittest.main()
