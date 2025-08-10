def get_translation(key: str, lang: str = "sr") -> str:
    translations = {
        "sr": {
            "upload_schema": "Otpremi elektro šemu",
            "schema_name": "Naziv šeme",
            "analyze_schema": "Analiziraj šemu",
            "save": "Sačuvaj",
            "preview": "Pregled šeme",
            "upload_doc": "Otpremi dodatnu dokumentaciju",
            "doc_name": "Naziv dokumentacije",
        },
        "en": {
            "upload_schema": "Upload electrical schematic",
            "schema_name": "Schema name",
            "analyze_schema": "Analyze schema",
            "save": "Save",
            "preview": "Schema preview",
            "upload_doc": "Upload additional documentation",
            "doc_name": "Documentation name",
        }
    }

    return translations.get(lang, {}).get(key, key)
