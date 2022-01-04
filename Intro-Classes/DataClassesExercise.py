import dataclasses as dc
import datetime

@dc.dataclass
class Order:
    OrderID = int
    CustomerID = int
    SalespersonPersonID = int
    PickedByPersonID = int
    ContactPersonID = int
    BackorderOrderID = int
    OrderDate = datetime.date
    ExpectedDeliveryDate = datetime.date
    CustomerPurchaseOrderNumber = str
    IsUndersupplyBackordered = bool
    PickingCompletedWhen = datetime.datetime
    LastEditedBy = int
    LastEditedWhen = datetime.datetime

    def __gt__(self,other):
        return 

@dc.dataclass
class Customer:
    CustomerID = int
    CustomerName = int
    BillToCustomerID = int
    CustomerCategoryID = int
    BuyingGroupID = int
    PrimaryContactPersonID = int
    AlternateContactPersonID = int
    DeliveryMethodID = int
    DeliveryCityID = int
    PostalCityID = int
    CreditLimit = float
    AccountOpenedDate = datetime.date
    StandardDiscountPercentage = int
    IsStatementSent = bool
    IsOnCreditHold = bool
    PaymentDays = int
    PhoneNumber = str
    FaxNumber = str
    WebsiteURL = str
    DeliveryAddressLine1 = str
    DeliveryAddressLine2 = str
    DeliveryPostalCode = str
    DeliveryLocation = str
    PostalAddressLine1 = str
    PostalAddressLine2 = str
    PostalPostalCode = str
    LastEditedBy = int
    ValidFrom = datetime.datetime
    ValidTo = datetime.datetime

@dc.dataclass
class Invoice:
    InvoiceID = int
    CustomerID = int
    BillToCustomerID = int
    OrderID = int
    DeliveryMethodID = int
    ContactPersonID = int
    AccountsPersonID = int
    SalespersonPersonID = int
    PackedByPersonID = int
    InvoiceDate = datetime.date
    CustomerPurchaseOrderNumber = str
    IsCreditNote = bool
    DeliveryInstructions = int
    TotalDryItems = int
    TotalChillerItems = int
    ReturnedDeliveryData = str
    ConfirmedDeliveryTime = datetime.datetime
    ConfirmedReceivedBy = str
    LastEditedBy = int
    LastEditedWhen = datetime.datetime




