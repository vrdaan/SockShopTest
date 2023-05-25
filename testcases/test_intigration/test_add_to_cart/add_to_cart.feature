Feature: Check Add to cart

    Scenario: AddToCart -> Add Product to cart
        Given A customer open the website
        And   he register his account
        And   he login to website
        And   get user addresses
        And   user add the product to cart with quantity:1
        Then   verify its cart with quantity:1

    Scenario: UpdateCart -> Update Product Quantity
        Given A customer open the website
        And   get his cart detail
        When  he is updating the cart quantity:4
        Then  verify its cart with quantity:5