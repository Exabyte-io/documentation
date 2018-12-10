# Add new Payment Method

!!!warning "Warning: content with restricted access"
    All the information contained under the present documentation page is only relevant for Account Owners or Administrators, since only they have sufficient rights to view the content exposed herein and make the appropriate changes. We remind the reader that a user is always the Owner and full administrator of his own personal Account.

In order to add a new payment method, the user should first click on the "Create" button <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> at the top-right corner of the "Payment Methods" tab under the ["Billing" page](../ui/charges-payments.md), and should then fill in the form appearing underneath it which has the following aspect:

![Add new Payment Method](../../images/accounts/add-new-payment.png "Add new Payment Method")

In the form shown above, the user should enter the appropriate Credit Card details on the panel to the left, and also insert the relevant information about the  Billing Address associated with the same Credit Card on the right-hand panel.
 
!!!note "Note: Credit Card data confidentiality"
     Any Credit Card information is never stored on our platform. All payments are in fact executed directly through the "stripe.com" service.

## Finalize Addition of new Payment Method

To finalize the addition of the new Credit Card as a future payment option, the user should click on the bottom `Add Card` button, or alternatively he/she should click a second time on the "Create" button (which will at this stage appear as a "minus" sign instead of the original "plus" sign) to negate all changes made to the Credit Card information being currently inserted.

Once a new Credit Card payment method has been added, it will be shown in the overall list under the "Payment Methods" tab for future reference, and it will be delegated as the default method of payment for all future transactions.

## Animation

In the example animation below, we demonstrate how to add a new Credit Card payment method by filling the resulting forms with some arbitrary information. The card finally appears as a new entry in the list of Cards at the top of the page:

<img data-gifffer="/images/accounts/add-credit-card.gif" />

## Set Default or Remove Payment Method

If multiple payment methods are stored under the same account, the default choice that will be used when crediting the account in all future transactions can be selected from the first column of the list under the "Payment Methods" tab page.

Any Credit Card payment method can furthermore be removed from the account's list by clicking on `Remove` in the correct entry row.

The location of both the "Set Default" and "Remove" features in the list of payment methods is highlighted in the below image:

![Remove Default Payment](../../images/accounts/remove-default-payment.png "Remove Default Payment")
