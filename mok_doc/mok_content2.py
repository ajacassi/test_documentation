import requests


class MokClass:
    """
    attributes:
        start (bool): start as False
    """

    def __init__(self):
        self.start = False

    def mok_text2(self, var1: int, var2: str, **kwargs) -> list:
        """
        testo della prima funzione

        Args:
            var1 (int): intero prima var
            var2 (int): intero seconda var
            **kwargs: additional parameters

        Keyword Args:
            skip (int, optional): numero di oggetti che si vogliono saltare nella risposta. Default to 0.
            limit (int, optional): numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.
            count (bool, optional): Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.
            like (bool, optional): Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.
            sort_by (str, optional): Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".
            null_fileds (str, optional): Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".
            type (str, optional): additional filter
            code (str, optional): additional filter
            company_name (str, optional): additional filter
            address (str, optional): additional filter
            zip_code (str, optional): additional filter
            city (str, optional): additional filter
            country (str, optional): additional filter
            notes (str, optional): additional filter
            vat_id (str, optional): additional filter
            currency (str, optional): additional filter
            state_province (str, optional): additional filter
            status (str, optional): additional filter

        Example:
            mok_text(1, 'ciao') = [1, 'ciao']

        Returns:
            rspense (List): risposta
        """
        self.start = True
        return [var1, var2]

    def mok_text3(self, var1: int, var2: str, **kwargs) -> list:
        """
        testo della prima funzione

        Args:
            var1 (int): intero prima var
            var2 (int): intero seconda var

        Returns:
            rspense (List): risposta
        """
        self.start = True
        return [var1, var2]