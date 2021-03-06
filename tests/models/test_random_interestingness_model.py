import pytest
from haste_storage_client.models.random_interestingness_model import RandomInterestingnessModel
from pytest import skip


class TestRandomInterestingnessModel:
    args1 = {'substream_id': 'stream_id_123',
             'timestamp': 12345,
             'location': (1, 2),
             'metadata': {
                 'foo': 1,
                 'bar': 2
             },
             'mongo_collection': None}

    def test_model_valid_result(self):
        model = RandomInterestingnessModel()
        result1 = model.interestingness(**self.args1)

        assert isinstance(result1, dict)
        assert 'interestingness' in result1
        assert 0 <= result1['interestingness'] <= 1.0

    # Bug: for some reason, the hash is inconsistent with pre-Python 3.5, so skip this for now.
    @pytest.mark.skip
    def test_hash_consistency(self):
        model = RandomInterestingnessModel()
        result1 = model.interestingness(**self.args1)
        assert result1['interestingness'] == 0.861

    def test_distinct_hash(self):
        model = RandomInterestingnessModel()

        args2 = self.args1.copy()
        # Changing a single field should be enough for a different hash:
        args2['timestamp'] = 6789

        result2 = model.interestingness(**args2)
        assert 0 <= result2['interestingness'] <= 1.0


        result1 = model.interestingness(**self.args1)
        assert result1 != result2
