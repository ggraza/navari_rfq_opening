## ERPNext Extensions on Request for Quotation and Supplier Quotation to include Committee Bid Openings

## Features

#### Committee

By using the Committee DocType, the system allows a user to set up a quote/bid opening committee and its members, who will open quotes or bids once the opening date and time are due. It can also be used to set up the Evaluation Committee for Supplier Quotations.
![rfq_opening_committee](https://github.com/user-attachments/assets/5cd8574a-6044-436a-a19a-19b361060b95)

![evaluation_committee](https://github.com/user-attachments/assets/14d7a4f8-2ccf-4bf2-883d-5440c8ab4368)


#### Committee Note

The system allows the generation of Committee Notes using predefined templates. The user can choose any template from the following options: Opening Minutes, Committee Register, and Evaluation Minutes. The templates are editable, allowing flexibility.
![committee_note](https://github.com/user-attachments/assets/83abdc54-9570-42c3-a98d-6fbf87e0e8f7)

## Process Flow

**Committee:**
Set up committees for both quote/bid opening and evaluation.

**Setting Closing Date, and quote opening committee on Request for Quotation**
![rfq2](https://github.com/user-attachments/assets/b67ec38b-240e-4e4b-b972-8e61c908cc57)

**Supplier Quotations Opening:**
At the time RFQs are being sent to suppliers, a ToDo record is created for each committee member, who will access it on the opening date and time, and open the quotes submitted against the RFQ. Supplier quotations are only accessible, after they have been opened by all the comittee members set for the RFQ.

**Committee Note:**
After opening the quotes, the desired committee note can be created.

### Installation

Using bench, [install ERPNext](https://github.com/frappe/bench#installation) as mentioned here.

Once ERPNext is installed, add rfq_opening_process app to your bench by running

```sh
$ bench get-app https://github.com/navariltd/rfq_opening_process.git
```

After that, you can install rfq_opening_process app on required site by running

```sh
$ bench --site [site.name] install-app rfq_opening_process
```

#### License

GNU General Public License (v3)
