Feature: Place Order Flow

    Scenario: PlaceOrder -> User Places the order
        Given A customer open the website
        And   he register his account
        And   he login to website
        And   user add the product to cart with quantity:1
        When  he verify its cart with quantity:1
        Then  he adds his address
        And   he adds the payment card
        And   he check the card detail
        When  he is done, he places the order
        Then  he verify the order details