# -*- coding: utf-8 -*-
import logging
from .base import Base
from .common import KeyWords, Tokens
from pyparsing import Forward
from typing import Any, Dict

_logger = logging.getLogger(__name__)  # type: ignore


class UtilBase(Base):
    def __init__(self, statement: str) -> None:
        super(UtilBase, self).__init__(statement)


"""
Syntext of list DDB tables:
{LIST | SHOW} TABLES

Sample SQL of Listing Tables:
-----------------------------
LIST TABLES
SHOW TABLES
"""


class UtilListTables(UtilBase):
    _LIST_TABLES_STATEMENT = ((KeyWords.LIST | KeyWords.SHOW) + KeyWords.TABLES)(
        "list_tables_statement"
    ).set_name("list_tables_statement")

    _UTIL_LIST_TABLES_EXPR = Forward()
    _UTIL_LIST_TABLES_EXPR <<= _LIST_TABLES_STATEMENT

    def __init__(self, statement: str) -> None:
        super(UtilListTables, self).__init__(statement)

    @property
    def syntex_def(self) -> Forward:
        return UtilListTables._UTIL_LIST_TABLES_EXPR

    def transform(self) -> Dict[str, Any]:
        return None


"""
Syntext of describe DDB table:
{DESC | DESCRIBE} tbl_name

Sample SQL of Describing Table:
-----------------------------
DESC Issues
DESCRIBE Issues
"""


class UtilDescTable(UtilBase):
    _DESC_TABLE_STATEMENT = ((KeyWords.DESC | KeyWords.DESCRIBE) + Tokens.TABLE_NAME)(
        "desc_table_statement"
    ).set_name("desc_table_statement")

    _DESC_TABLE_EXPR = Forward()
    _DESC_TABLE_EXPR <<= _DESC_TABLE_STATEMENT

    def __init__(self, statement: str) -> None:
        super(UtilDescTable, self).__init__(statement)

    @property
    def syntex_def(self) -> Forward:
        return UtilDescTable._DESC_TABLE_EXPR

    def transform(self) -> Dict[str, Any]:
        if self.root_parse_results is None:
            raise ValueError("Statement was not parsed yet")

        request = dict()
        request.update({"TableName": self.root_parse_results["table"]})

        return request
