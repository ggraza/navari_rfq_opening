## ERPNext Extensions on Request for Quotation and Supplier Quotation to include Committee Bid Openings

## Features

### Committee

By using the Committee DocType, the system allows a user to set up a quote/bid opening committee and its members, who will open quotes or bids once the opening date and time are due. It can also be used to set up the Evaluation Committee for Supplier Quotations.

### Committee Note

The system allows the generation of Committee Notes using predefined templates. The user can choose any template from the following options: Opening Minutes, Committee Register, and Evaluation Minutes. The templates are editable, allowing flexibility."

## Process Flow

**Committee**
Set up committees for both quote/bid opening and evaluation.

**Setting Closing Date, and quote opening committee on Request for Quotation**
![image](https://github.com/navariltd/navari_rfq_opening/assets/1822868/9ee5ac7b-fa73-4fb2-be17-97930154bfe8)

**Supplier Quotations Opening**
At the time RFQs are being sent to suppliers, a ToDo record is created for each committee member, who will access it on the opening date and time, and open the quotes submitted against the RFQ. Supplier quotations are only accessible, after they have been opened by all the comittee members set for the RFQ.

**Committee Note**
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
