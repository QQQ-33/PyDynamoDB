# -*- coding: utf-8 -*-
from pydynamodb.model import ColumnInfo, Metadata


class TestModel:
    def test_metadata_iter(self):
        col1 = ColumnInfo("col1", "col1", alias="col1_alias")
        col2 = ColumnInfo("col2", "col2", "col2_alias")
        metadata = Metadata()
        metadata.update(col1)
        metadata.update(col2)

        assert len(metadata) == 2
        assert [m for m in metadata] == [col1, col2]
        assert metadata["col1"] == col1
        assert metadata.get("col2", None) == col2
        assert metadata.get("col3", None) is None
        assert metadata.index("col2") == 1
        assert "col1" in metadata
        assert "col3" not in metadata

        metadata.clear()
        assert len(metadata) == 0
