# ERPNext Extensions on Request for Quotation and Supplier Quotation to include Committee Bid Openings

## Overview

This app extends the standard Request for Quotation (RFQ) functionality in ERPNext by introducing enhancements to streamline the procurement process. It enables committee bid openings and the creation of committee notes based on predefined templates.

## Features

### 1. Custom Fields in Request for Quotation(RFQ)

The following fields have been introduced to the RFQ DocType.

| Field Name              | Type | Description                       |
| :---------------------- | :--- | :-------------------------------- |
| committee               | Link | Quotation opening committee       |
| minimum_expected_quotes | Date | Minimum number of expected quotes |
| closing_time            | Time | Closing time for the RFQ          |
| closing_date            | Date | Closing date for the RFQ          |

### 2. Custom Fields in Supplier Quotation

The following fields have been introduced to the Supplier Quotation DocType.

| Field Name        | Type   | Description                                |
| :---------------- | :----- | :----------------------------------------- |
| submission_status | Select | Submission status for a supplier quotation |

### 3. RFQ Opening Settings

This DocType contains global settings for RFQ and includes the following check fields.

| Field Name                                     | Type  | Description                                                         |
| :--------------------------------------------- | :---- | :------------------------------------------------------------------ |
| allow_multiple_supplier_quotations_from_portal | Check | Checked if suppliers are allowed to provide multiple quotations     |
| skip_supplier_quotation_opening_by_committee   | Check | Checked if you want to skip supplier quotation opening by committee |
| ignore_default_buying_price_list_validation    | Check | Checked if you want to ignore default buying price list validation  |

### 4. New DocType: Committee

This DocType allows the setup of both Quotation Opening and Evaluation Committees. It includes the following fields:

| Field Name                           | Type        | Description                                               |
| :----------------------------------- | :---------- | :-------------------------------------------------------- |
| committee_name                       | Data        | Name of committee                                         |
| disabled                             | Check       | Checked if the committee is disabled                      |
| opening_minutes                      | Check       | Checked if committee is applicable for Opening Minutes    |
| committee_register                   | Check       | Checked if committee is applicable for Committee Register |
| evaluation_minutes                   | Time        | Checked if committee is applicable for Evaluation Minutes |
| minimum_no_of_members_needed_to_open | Int         | Minimum number of members needed to open a quote          |
| description                          | Text Editor | Description of the committee                              |
| committee_members                    | Table       | Table for the committee members                           |

### 5. Committee Member

This is a child DocType of the Committee DocType that stores the committee members. It includes the following fields:

| Field Name | Type      | Description           |
| :--------- | :-------- | :-------------------- |
| user_id    | Link      | Link to User          |
| full_name  | Read Only | Full name of the User |
| signature  | Attach    | signature of the User |

### 6. Committee Note

This DocType allows the creation of Committee Notes after the Quotation Opening Committee has opened the quotations. It includes the following fields.

| Field Name           | Type        | Description                                               |
| :------------------- | :---------- | :-------------------------------------------------------- |
| series               | Select      | Naming series for the document                            |
| quotation            | Link        | Quotation for which you want to create the committee note |
| date                 | Date        | Date of the committee note                                |
| committee            | Link        | Committee picked on the RFQ                               |
| note_type            | Select      | Select field for the committee note template              |
| evaluation_committee | Link        | Evaluation Committee for the quotations                   |
| generated_content    | Text Editor | Editable content generated from templates                 |
| committee_members    | Table       | Table for the committee members                           |

# Configuration

- Navigate to **RFQ Opening Settings** and configure the necessary parameters.

  ![Screenshot from 2025-02-27 17-04-47](https://github.com/user-attachments/assets/15feb853-d37b-4f42-8f2e-befeb5438509)

- Set up the **Quotation Opening** and **Evaluation** committees under the Committee DocType, and select the templates to which the committees apply by ticking the necessary checkbox.

  #### Quotation Opening Committee

  ![Screenshot from 2025-02-27 17-02-40](https://github.com/user-attachments/assets/e7242579-639b-4f9c-a336-fe329e15ff06)

  #### Evaluation Committee

  ![Screenshot from 2025-02-27 17-03-16](https://github.com/user-attachments/assets/6795f316-4b4b-46e1-a248-e758b7c6e8db)

# Usage

### Create an RFQ

Go to **Request for Quotation** and create a new RFQ. Select the Quotation Opening Committee, specify the closing date, closing time, and minimum expected quotes. Add the suppliers who will receive the RFQ, include the items, then save and submit. When RFQs are sent to suppliers, a ToDo record is created for each committee member. On the opening date and time, committee members can access their ToDo records and open the submitted quotes against the RFQ.

![Screenshot from 2025-02-27 17-07-25](https://github.com/user-attachments/assets/00dfbfb4-beaa-4b22-852e-f2edb1ba0f6b)

### Supplier Quotations Opening

Once the closing date and time for the RFQ are reached, committee members can access the RFQ and open the submitted quotes. Supplier quotations become accessible only after the minimum required number of members has opened them, as set for the RFQ.

### Create Committee Note

Navigate to the **Committee Note** and create a new entry. Select the specific RFQ for which you want to create the Committee Note, choose the note type, and set the date (which defaults to today). The quotation opening committee will be fetched automatically from the selected RFQ.
Three types of committee notes can be created from predefined templates:

- **Opening Minutes**: Records of the quotation opening committee's proceedings.

  ![Screenshot from 2025-02-27 17-58-31](https://github.com/user-attachments/assets/8b46706a-e960-4987-9775-11edfa0fc65d)

- **Committee Register**: A register of members present during the evaluation.

  ![Screenshot from 2025-02-27 17-59-15](https://github.com/user-attachments/assets/05aff445-ccd9-4cc3-9c2b-33878700d2b3)

- **Evaluation Minutes**: Minutes documenting the evaluation of supplier quotations.

  ![Screenshot from 2025-02-27 17-57-33](https://github.com/user-attachments/assets/b518e1b4-c03f-4504-9aa3-7b4f9717a11f)

# Manual Installation

Using bench, [install ERPNext](https://frappecloud.com/marketplace/apps/erpnext) as mentioned here.

Once ERPNext is installed, add rfq_opening_process app to your bench by running

```sh
$ bench get-app https://github.com/navariltd/rfq_opening_process.git
```

After that, you can install rfq_opening_process app on required site by running

```sh
$ bench --site [site.name] install-app rfq_opening_process
```

# Frappe Cloud Installation

## Steps to Install an App

1. **Log in to Frappe Cloud**

   - Visit [Frappe Cloud](https://frappecloud.com/) and sign in.

2. **Setup a [bench](https://frappecloud.com/docs/benches/create-new).**

3. **Go to the Apps Section of your bench**

   - Open the bench dashboard and click on the **Apps** tab. Click on **Add App** and add RFQ Opening Process from marketplace or from GitHub.
   - Deploy the app.

4. **On your bench, create a new site**

5. **Go to the Apps Section of your site**

   - Browse available apps or search for RFQ Opening Process.

6. **Click Install**

   - Select the app and click the **Install** button.

7. **Wait for Installation**

   - The installation process will take a few moments. Once complete, the app will be available on your site.

8. **Verify Installation**
   - Open your site, navigate to the **Modules** section, and check if the app appears in the list.

# License

GNU General Public License (v3)

# Contact

For inquiries or support, please contact us at [support@navari.co.ke]
