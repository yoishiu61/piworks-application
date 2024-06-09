# User Interface Specification Document for PIWorks

## 1. INTRODUCTION

I have prepared a document in markdown format to explain the functions and specifications of the desired userface image that can be seen [here](https://lists.office.com/Images/969df1bb-97b6-44ef-9108-dc18a5fd96c2/298428f6-6729-4501-a9de-dcaf554877fe/T3L0G2MKUPU8GQUY8YHP00Z9RB/c2f1cb7e-5022-433a-93a2-1ac0b6ec1015).

![Example UI image](https://lists.office.com/Images/969df1bb-97b6-44ef-9108-dc18a5fd96c2/298428f6-6729-4501-a9de-dcaf554877fe/T3L0G2MKUPU8GQUY8YHP00Z9RB/c2f1cb7e-5022-433a-93a2-1ac0b6ec1015)

*Provided image of desired UI.*

## 2. REQUIREMENTS

- UI for creating, listing and modifying user accounts. When accessed, all fields will fit the same screen.
	- List the accounts with the ID number, username, e-mail and enabled status fields.
	- Sorting for the fields mentioned.
	- Filters for the fields mentioned.
- Checkbox for hiding disabled accounts
- Fields for creating/modifying user accounts.

## 3. UI ELEMENTS

There is three main sections in the UI. Ribbon, left half and right half. Ribbon has two buttons and one tick box. Left half will have the accounts list. Right half will have the fields to edit/create accounts.

### RIBBON

The ribbon field will include:

* **NEW ACCOUNT** button on the left.
* **HIDE DISABLED USER** tick box. Hides users from list if "Enabled" field is "false".
* **SAVE ACCOUNT** button on the right. Commits changes. Grayed out when requirements are unmet.


### LEFT HALF (LIST)

The left half will have the accounts listed.
There will be FOUR COLUMNS.

1) **ID:** Number appointed at account creation.
2) **USER NAME:** Text field describing account.
3) **EMAIL:** Text field with email address.
4) **ENABLED:** Boolean field describing if account is enabled or not. True if enabled.

Each column should have **FILTER AND SORT** options. Sorting will be alphabetical and filtering should have different behaviour for different columns. 

When clicking on **COLUMN NAMES**, change the sort to that column. If already selected reverse sort type. Implement visual cue.

Implement visual cue to show if a **FILTER** is active.

Prefferably, implement **clear all filters** button.

1) **ID:** Filter with text search.
2) **USER NAME:** Filter with text search. Since no formatting is enforced, 
3) **EMAIL:** Filter with text search.
4) **ENABLED:** Filter with tick boxes for "true" and "false".

When **SELECTED**, accounts on the list should be **HIGHLIGHTED** for clarity. When no account is selected, nothing should be highlighted.

### RIGHT HALF (ACCOUNT DETAILS)

The right half is for creating/modifying accounts.
List items, when selected, should display their information in these fields.
Prefferably, put asterisk to showcase the required fields. Grayed out text in the right half to explain the asterisk can also be useful.

1) **Username:** Text field describing account. Same as in list. Spaces allowed. Length limit of 50 characters. Alphanumerical allowed.
2) **Display Name:** Text field for further description. Not required. Spaces allowed. Length limit of 50 characters. Alphanumerical allowed.
3) **Phone:** Number field for phone. Input masking to guide for correct format. Example: (555) 555 55 55. Correct format required for saving.
4) **Email:** Text field with email address. Same as in list. Correct format required for saving.
5) **User Roles:** Drop down menu with three options:
	* Guest
	* Admin
	* SuperAdmin
	
	Correct format required for saving.
6) **Enabled:** Enabled status of the account. Tick if enabled. Tick = true for list.

The following fields are **REQUIRED** to have information to save:
* **USERNAME:** Should not be empty and be in the correct format.
* **EMAIL:** Should not be empty and be in the correct format.
* **USER ROLES:** Should be selected. Avoiding default value will promote correct usage.

## 4. INTERACTION SCENARIO

Intended interaction will be as such:

* User should be able to see the entire UI at once.
* Default state of "hide disabled user" tick box should be unticked.
* Default sorting is by ID number.
* If fields are filled incorrectly, change the field outline to red and/or show a warning text.
* The save user button should be grayed out when fields aren't filled correctly or the required fields are empty.

### WARNINNG POP-UPS

* Since only Admin / SuperAdmin accounts can reach this page, show **WARNING POP-UP** when changing **Enabled Status** for these accounts, especially if the user is trying to change **THEIR OWN Enabled Status**.
* If there are unsaved changes, reloading the page, selecting another account from the list or clicking the new account button should create a **WARNING POP-UP**.

Enter or ESC key should close the pop-up windows and abort saving / reloading / proceeding without saving. Arrow keys, tab key or clicking should be required to commit these actions with the pop-up window.

### Optional Changes
* ESC key binded to unselect account, this clears the fields on the right. 
	* If this change has been implemented, show pop-up as described above.
* Ctrl + Enter (or other commonly used bind) binded to save account.
* Arrow keys to navigate between accounts on list. (full row selected)

