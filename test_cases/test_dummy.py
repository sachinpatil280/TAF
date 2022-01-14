import pytest


class Test:

    @pytest.mark.sanity
    def test_dummy_001(self, ui):
        try:
            ui.dummy_page.get_page_title()
        except Exception as e:
            pytest.fail(e)
        finally:
            ui.close()
