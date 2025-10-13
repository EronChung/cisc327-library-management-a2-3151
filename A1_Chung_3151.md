**CISC327 A1 (Fall 2025)**  
Eron Chung (20393151)  
Group 1  

---

| Func. Req.    | Implementation Status | Notes
| ------------- | --------------------- | -----
| R1            | Complete              | None
| R2            | Complete              | None
| R3            | Complete              | None
| R4            | Incomplete            | Missing all functionality; only HTML fields/buttons exist.
| R5            | Partial               | api route exists, but the called function `calculate_late_fee_for_book` is not yet implemented. <br>Additionally, the route is unused anywhere.
| R6            | Incomplete            | Missing all functionality; only HTML fields/buttons exist.
| R7            | Partial               | Missing functionality on the site, <br>but relevant functions are implemented in `database.py`.

---

### Unit Tests

Test files are located in `tests` subfolder,  
although they will not run from in there since the  
`from ... import` is wrong (must bring them out).  

Each file runs several tests on the function mention in the name.  
All of the tested functions are from `library_service.py`.  

`test_add_book_to_catalog.py`  
`test_borrow_book_by_patron.py`  
`test_return_book_by_patron.py`  
`test_calculate_late_fee_for_book.py`  
`test_search_books_in_catalog.py`  
`test_get_patron_status_report.py`  