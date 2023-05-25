To run the test cases and start the server using the provided commands, you can follow these steps:

1. Open a terminal or command prompt.

3. Navigate to the `SockShopTest` folder using the `cd` command:
   ```
   cd SockShopTest
   ```

3. Start the server by running the Docker Compose command:
   ```
   docker-compose -f deploy/docker-compose/docker-compose.yml up -d
   ```
   Wait for the Docker containers to start up. The `-d` flag runs the containers in the background.

4. Once the server is up and running, open a new terminal or command prompt (while keeping the previous one running) and navigate to the `SockShopTest` folder again.

5. Run the tests using the `pytest` command:
   ```
   pytest
   ```
   This command will automatically discover and run the test cases.
   Make sure you have the necessary dependencies installed, such as `pytest` and `pytest_bdd` . Additionally, ensure that Docker is installed and running properly on your machine at `localhost`. Also we are not using `mock-db` which get purged after every run, so we have to update email on next run, or we can purge the db.

6. Below is the postman collection to verify the flow and api's testing using postman.
  ```
  https://api.postman.com/collections/11289161-1e60baff-8000-4e5e-8555-4983f4cce352?access_key=PMAT-01H194WJGA64XWTPRP52NCCBTW
  ```
  1. Import the collection in postman
  2. Set the collection variables by clicking on collection
  3. Run the collection by `Run Collection` and verify the test cases once run is completed.
  
  MakeSure not to update the Order of the API's as some API's are updating parameters which are required in next API's
