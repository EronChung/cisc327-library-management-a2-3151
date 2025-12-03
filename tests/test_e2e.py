from playwright.sync_api import Page, expect


def test_user_flow_1(page):
    """Test the following flow:
    - Add a new book
    - Borrow a copy of the book
    - Check if borrow popup appears
    """

    page.goto("http://localhost:5000")

    # Quick preliminary check if page is correct (via title)
    assert page.title() == "Library Management System"
    
    # Go to add new book page
    page.get_by_text("➕ Add New Book").click()

    # Fill fields and submit
    page.locator("#title"       ).fill("My New Book")
    page.locator("#author"      ).fill("Some Author")
    page.locator("#isbn"        ).fill("1234567890123")
    page.locator("#total_copies").fill("5")
    page.get_by_text("Add Book to Catalog").click()

    # Borrow book
    page.get_by_role("row", name="4 My New Book Some Author").get_by_placeholder("Patron ID (6 digits)").fill("123456")
    page.get_by_role("row", name="4 My New Book Some Author").get_by_role("button").click()

    # Check for borrow book confirmation
    assert page.get_by_text("Successfully borrowed").count() == 1


def test_user_flow_2(page):
    """Test the following flow:
    - Return a book
    - Return a book that is not being borrowed
    """

    page.goto("http://localhost:5000")

    # Quick preliminary check if page is correct (via title)
    assert page.title() == "Library Management System"

    # Go to return a book page
    page.get_by_role("link", name="↩️ Return Book").click()

    # Return the book borrowed from previous test
    page.get_by_role("textbox", name="Patron ID *").fill("123456")
    page.get_by_role("spinbutton", name="Book ID *").fill("4")
    page.get_by_role("button", name="Process Return").click()

    # Check for return book confirmation
    assert page.get_by_text("Successfully returned").count() == 1

    # Return a book not being borrowed
    page.get_by_role("textbox", name="Patron ID *").fill("123456")
    page.get_by_role("spinbutton", name="Book ID *").fill("1")
    page.get_by_role("button", name="Process Return").click()

    # Check for error popup
    assert page.get_by_text("not currently borrowing").count() == 1