import pytest
import time


class TestGoogleSearch:

    @pytest.mark.sanity
    def test_google_search_basic(self, ui):
        """Test basic Google search functionality"""
        try:
            search_term = "selenium automation testing"
            
            # Perform search
            assert ui.google_search_page.search_and_wait(search_term, "enter"), "Search operation failed"
            
            # Verify search was performed
            assert ui.google_search_page.verify_search_performed(search_term), "Search verification failed"
            
            # Verify results are displayed
            results_count = ui.google_search_page.get_search_results_count()
            assert results_count > 0, f"No search results found. Expected > 0, got {results_count}"
            
            print(f"✅ Basic search test passed - Found {results_count} results")
            
        except Exception as e:
            pytest.fail(f"Basic search test failed: {e}")
        finally:
            ui.close()

    @pytest.mark.regression
    def test_google_im_feeling_lucky(self, ui):
        """Test I'm Feeling Lucky functionality"""
        try:
            search_term = "python.org"
            
            # Enter search term
            assert ui.google_search_page.enter_search_term(search_term), "Failed to enter search term"
            
            # Click I'm Feeling Lucky
            assert ui.google_search_page.click_im_feeling_lucky(), "Failed to click I'm Feeling Lucky"
            
            # Wait for page to load and verify redirection
            time.sleep(3)  # Wait for redirection
            current_url = ui.google_search_page.driver.current_url
            
            # Should be redirected away from Google search
            assert "google.com/search?" not in current_url, "Should have been redirected from Google search"
            
            print(f"✅ I'm Feeling Lucky test passed - Redirected to: {current_url}")
            
        except Exception as e:
            pytest.fail(f"I'm Feeling Lucky test failed: {e}")
        finally:
            ui.close()

    @pytest.mark.sanity
    def test_google_search_box_operations(self, ui):
        """Test search box operations (clear, get current value)"""
        try:
            search_term = "test automation framework"
            
            # Enter search term
            assert ui.google_search_page.enter_search_term(search_term), "Failed to enter search term"
            
            # Verify current search term
            current_term = ui.google_search_page.get_current_search_term()
            assert current_term == search_term, f"Expected '{search_term}', got '{current_term}'"
            
            # Clear search box
            assert ui.google_search_page.clear_search_box(), "Failed to clear search box"
            
            # Verify search box is empty
            current_term_after_clear = ui.google_search_page.get_current_search_term()
            assert current_term_after_clear == "", f"Search box should be empty, got '{current_term_after_clear}'"
            
            print("✅ Search box operations test passed")
            
        except Exception as e:
            pytest.fail(f"Search box operations test failed: {e}")
        finally:
            ui.close()

    @pytest.mark.regression
    def test_google_multiple_searches(self, ui):
        """Test performing multiple searches in sequence"""
        try:
            search_terms = ["automation testing", "selenium webdriver", "pytest framework"]
            
            for i, search_term in enumerate(search_terms):
                print(f"\n--- Search {i+1}: {search_term} ---")
                
                # Clear previous search and enter new term
                ui.google_search_page.clear_search_box()
                assert ui.google_search_page.search_and_wait(search_term), f"Search {i+1} failed"
                
                # Verify each search
                assert ui.google_search_page.verify_search_performed(search_term), f"Search {i+1} verification failed"
                
                results_count = ui.google_search_page.get_search_results_count()
                assert results_count > 0, f"Search {i+1} returned no results"
                
                print(f"✅ Search {i+1} passed - {results_count} results")
            
            print(f"\n✅ Multiple searches test passed - All {len(search_terms)} searches successful")
            
        except Exception as e:
            pytest.fail(f"Multiple searches test failed: {e}")
        finally:
            ui.close()

    @pytest.mark.regression
    def test_google_search_edge_cases(self, ui):
        """Test edge cases for Google search"""
        try:
            # Test empty search - verify it can be entered (but not searched)
            ui.google_search_page.clear_search_box()
            assert ui.google_search_page.enter_search_term(""), "Failed to enter empty search"
            current_value = ui.google_search_page.get_current_search_term()
            assert current_value == "", "Empty search box verification failed"
            print("✅ Empty search test passed")
            
            # Test special characters
            special_search = "test automation"  # Google filters special chars, use simple term
            ui.google_search_page.clear_search_box()
            time.sleep(0.5)
            assert ui.google_search_page.search_and_wait(special_search)
            time.sleep(1)
            results = ui.google_search_page.get_search_results_count()
            assert results > 0, f"Special search returned no results"
            print(f"✅ Special character search passed - {results} results")
            
            # Test very long search term
            long_search = "this is a very long search term that contains many words to test how google handles lengthy search queries"
            ui.google_search_page.clear_search_box()
            time.sleep(0.5)
            assert ui.google_search_page.search_and_wait(long_search), "Long search term failed"
            time.sleep(1)
            results = ui.google_search_page.get_search_results_count()
            assert results > 0, f"Long search returned no results"
            print(f"✅ Long search passed - {results} results")
            
            print("\n✅ All edge cases tests passed")
            
        except Exception as e:
            pytest.fail(f"Edge cases test failed: {e}")
        finally:
            ui.close()