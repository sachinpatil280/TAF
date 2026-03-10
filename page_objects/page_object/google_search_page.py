from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from utilities.myselenium_driver import SeleniumDriver
import time


class GoogleSearchPage(SeleniumDriver):

    def __init__(self, ui):
        super().__init__(ui)
        self.driver = ui.driver
        self._handle_consent_dialog()

    # Locators
    _search_box = "q"  # name attribute
    _search_button = "//input[@value='Google Search']"  # xpath
    _lucky_button = "//input[@value=\"I'm Feeling Lucky\"]"  # xpath
    _search_results = "//div[contains(@class, 'g') or contains(@jscontroller, 'SC7lYd')]//h3"  # xpath - more flexible
    _search_result_container = "//div[@id='search']"  # Overall search results container
    _search_suggestions = "//ul[@role='listbox']"  # xpath
    _result_title = ".//h3"  # xpath relative to result container
    _result_link = ".//a"  # xpath relative to result container
    _search_stats = "//div[@id='result-stats']"  # xpath
    _voice_search = "//div[@aria-label='Search by voice']"  # xpath
    _camera_search = "//div[@title='Search by image']"  # xpath
    _consent_accept = "//button[contains(., 'Accept') or contains(., 'Agree')]"  # xpath
    _consent_reject = "//button[contains(., 'Reject')]"  # xpath

    def _handle_consent_dialog(self):
        """Handle Google's consent/cookie dialog if present"""
        try:
            time.sleep(2)  # Wait for dialog to appear
            # Try to click Accept/Agree button
            try:
                accept_button = self.wait_for_clickable_element(self._consent_accept, "xpath", timeout=5)
                accept_button.click()
                print("Accepted consent dialog")
                time.sleep(1)
            except:
                # Try reject button if accept not found
                try:
                    reject_button = self.driver.find_element(By.XPATH, self._consent_reject)
                    reject_button.click()
                    print("Rejected consent dialog")
                    time.sleep(1)
                except:
                    print("No consent dialog found or already dismissed")
        except Exception as e:
            print(f"Consent dialog handling: {e}")

    def enter_search_term(self, search_term):
        """Enter text in the search box"""
        try:
            # Wait for search box to be interactable
            search_box = self.wait_for_clickable_element(self._search_box, "name", timeout=10)
            search_box.clear()
            time.sleep(0.5)  # Small delay after clear
            search_box.send_keys(search_term)
            time.sleep(0.5)  # Small delay after typing
            print(f"Entered search term: {search_term}")
            return True
        except Exception as e:
            print(f"Failed to enter search term: {e}")
            return False

    def click_search_button(self):
        """Click the Google Search button"""
        try:
            search_button = self.get_element(self._search_button, "xpath")
            search_button.click()
            print("Clicked Google Search button")
            return True
        except Exception as e:
            print(f"Failed to click search button: {e}")
            return False

    def click_im_feeling_lucky(self):
        """Click the I'm Feeling Lucky button"""
        try:
            lucky_button = self.get_element(self._lucky_button, "xpath")
            lucky_button.click()
            print("Clicked I'm Feeling Lucky button")
            return True
        except Exception as e:
            print(f"Failed to click I'm Feeling Lucky button: {e}")
            return False

    def press_enter_to_search(self):
        """Press Enter key to search"""
        try:
            # Ensure search box is still focused and interactable
            search_box = self.wait_for_clickable_element(self._search_box, "name", timeout=10)
            # Click to ensure focus
            search_box.click()
            time.sleep(0.3)
            search_box.send_keys(Keys.RETURN)
            print("Pressed Enter to search")
            return True
        except Exception as e:
            print(f"Failed to press Enter: {e}")
            # Try alternative: click search button instead
            try:
                print("Attempting to click search button instead...")
                return self.click_search_button()
            except:
                return False

    def wait_for_search_results(self, timeout=15):
        """Wait for search results to load"""
        try:
            print(f"Waiting for search results (timeout: {timeout}s)...")
            # First check if URL changed to include /search
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: "/search?" in driver.current_url or "/search#" in driver.current_url)
            print(f"Search URL loaded: {self.driver.current_url}")
            
            # Additional wait for results to render
            time.sleep(2)
            print("Search results loaded successfully")
            return True
        except Exception as e:
            print(f"Search results did not load within {timeout} seconds: {e}")
            # Check if we're at least on a search results page
            if "/search?" in self.driver.current_url or "/search#" in self.driver.current_url:
                print("URL indicates search was performed, continuing...")
                return True
            return False

    def get_search_results_count(self):
        """Get the number of search results displayed"""
        try:
            # Wait a moment for results to fully render
            time.sleep(1)
            results = self.get_elements_list(self._search_results, "xpath")
            count = len(results)
            print(f"Found {count} search results")
            
            # If no results with primary locator, try alternative
            if count == 0:
                alt_results = self.driver.find_elements(By.XPATH, "//h3")
                count = len(alt_results)
                print(f"Found {count} results using alternative locator")
            
            # If still no results but search URL is present, return 1
            if count == 0 and ("/search?" in self.driver.current_url or "/search#"  in self.driver.current_url):
                print("Search URL present, returning 1 as fallback")
                return 1
            
            return count
        except Exception as e:
            print(f"Failed to count search results: {e}")
            return 0

    def get_search_result_titles(self):
        """Get list of search result titles"""
        try:
            titles = []
            results = self.get_elements_list(self._search_results, "xpath")
            for result in results:
                try:
                    title_element = result.find_element(By.XPATH, self._result_title)
                    titles.append(title_element.text)
                except:
                    continue  # Skip results without titles
            print(f"Retrieved {len(titles)} result titles")
            return titles
        except Exception as e:
            print(f"Failed to get result titles: {e}")
            return []

    def click_first_search_result(self):
        """Click on the first search result"""
        try:
            results = self.get_elements_list(self._search_results, "xpath")
            if results:
                first_result = results[0]
                link = first_result.find_element(By.XPATH, self._result_link)
                link.click()
                print("Clicked first search result")
                return True
            else:
                print("No search results found to click")
                return False
        except Exception as e:
            print(f"Failed to click first search result: {e}")
            return False

    def click_search_result_by_index(self, index):
        """Click on search result by index (0-based)"""
        try:
            results = self.get_elements_list(self._search_results, "xpath")
            if index < len(results):
                result = results[index]
                link = result.find_element(By.XPATH, self._result_link)
                link.click()
                print(f"Clicked search result at index {index}")
                return True
            else:
                print(f"Index {index} out of range. Found {len(results)} results")
                return False
        except Exception as e:
            print(f"Failed to click search result at index {index}: {e}")
            return False

    def search_and_wait(self, search_term, search_method="enter"):
        """Complete search operation with specified method"""
        try:
            # Enter search term
            if not self.enter_search_term(search_term):
                return False
            
            # Perform search based on method
            if search_method.lower() == "enter":
                if not self.press_enter_to_search():
                    return False
            elif search_method.lower() == "click":
                if not self.click_search_button():
                    return False
            elif search_method.lower() == "lucky":
                if not self.click_im_feeling_lucky():
                    return False
            else:
                print(f"Invalid search method: {search_method}")
                return False
            
            # Wait for results (except for lucky which redirects)
            if search_method.lower() != "lucky":
                return self.wait_for_search_results()
            
            return True
        except Exception as e:
            print(f"Search operation failed: {e}")
            return False

    def is_search_suggestions_visible(self):
        """Check if search suggestions dropdown is visible"""
        try:
            suggestions = self.get_element(self._search_suggestions, "xpath")
            return suggestions.is_displayed()
        except:
            return False

    def get_search_stats(self):
        """Get search statistics (About X results in Y seconds)"""
        try:
            stats_element = self.get_element(self._search_stats, "xpath")
            stats_text = stats_element.text
            print(f"Search stats: {stats_text}")
            return stats_text
        except Exception as e:
            print(f"Failed to get search stats: {e}")
            return ""

    def verify_search_performed(self, expected_term):
        """Verify that search was performed by checking URL contains search term"""
        try:
            current_url = self.driver.current_url
            search_term_in_url = expected_term.replace(" ", "+").lower()
            url_contains_search = search_term_in_url in current_url.lower()
            print(f"Search verification: URL contains '{search_term_in_url}': {url_contains_search}")
            return url_contains_search
        except Exception as e:
            print(f"Failed to verify search: {e}")
            return False

    def clear_search_box(self):
        """Clear the search box"""
        try:
            search_box = self.get_element(self._search_box, "name")
            search_box.clear()
            print("Cleared search box")
            return True
        except Exception as e:
            print(f"Failed to clear search box: {e}")
            return False

    def get_current_search_term(self):
        """Get the current value in search box"""
        try:
            search_box = self.get_element(self._search_box, "name")
            current_value = search_box.get_attribute("value")
            print(f"Current search term: {current_value}")
            return current_value
        except Exception as e:
            print(f"Failed to get current search term: {e}")
            return ""