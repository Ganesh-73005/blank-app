# **Order Processing System with Apache Camel and Drools**  

## **Overview**  
This project demonstrates an **order processing system** that integrates:  
- **Apache Camel** for routing and mediation  
- **Drools (KIE)** for business rule execution  
- **Spring Boot** for REST API and dependency injection  

The system processes orders by:  
1. Validating customer details using Drools rules  
2. Applying discounts and business logic based on order details  
3. Managing workflows using Camel routes  

---

## **Key Features**  
✅ **REST API** for order submission and processing  
✅ **File-based processing** for batch orders  
✅ **Drools rules engine** for dynamic business logic  
✅ **Error handling** with structured JSON responses  
✅ **JSON (de)serialization** using Jackson  

---

## **System Architecture**  

### **1. Components**  
| Component | Description |  
|-----------|------------|  
| **OrderController** | REST endpoint for order submission |  
| **OrderProcessingRoute** | Camel route for order processing |  
| **OrderProcessingService** | Service layer integrating Drools |  
| **DroolsConfig** | Configures KieContainer and sessions |  
| **JacksonConfig** | Custom JSON serialization settings |  

### **2. Workflow**  
```mermaid
flowchart TD
    A[HTTP POST /api/orders/process] --> B[Camel REST DSL]
    B --> C[direct:processOrder]
    C --> D[Unmarshal JSON to OrderRequest]
    D --> E[Validate Customer (Drools)]
    E --> F[Process Order (Drools)]
    F --> G[Build OrderResponse]
    G --> H[Marshal to JSON]
    H --> I[Return HTTP Response]

    J[File Input (input/orders)] --> K[Unmarshal JSON]
    K --> L[Same as REST flow]
    L --> M[Save to output/processed-orders]
```

---

## **API Endpoints**  

### **1. Submit an Order**  
- **Method**: `POST /api/orders/process`  
- **Request Body**:  
  ```json
  {
    "order": {
      "orderId": "ORD001",
      "customerId": "CUST001",
      "items": [
        {
          "productId": "PROD001",
          "name": "Laptop",
          "quantity": 1,
          "price": 999.99,
          "category": "Electronics"
        }
      ]
    },
    "customer": {
      "customerId": "CUST001",
      "name": "John Doe",
      "email": "john.doe@example.com",
      "membership": "PREMIUM",
      "loyaltyPoints": 1500
    }
  }
  ```
- **Response**:  
  ```json
  {
    "status": "SUCCESS",
    "message": "Order processed successfully",
    "order": {
      "orderId": "ORD001",
      "discountAmount": 100.00,
      "status": "APPROVED"
    },
    "customer": {
      "customerId": "CUST001",
      "validated": true
    }
  }
  ```

### **2. Get Sample Order (Testing)**  
- **Method**: `GET /api/orders/sample`  
- **Response**: Predefined sample order for testing.  

### **3. Health Check**  
- **Method**: `GET /api/test/health`  
- **Response**:  
  ```json
  { "status": "UP", "message": "Application is running" }
  ```

---

## **Drools Rule Sessions**  
Configured in `kmodule.xml`:  
```xml
<kbase name="orderProcessingKBase" packages="rules">
    <ksession name="orderProcessingSession" type="stateful" default="true"/>
    <ksession name="customerValidationSession" type="stateful"/>
</kbase>
```

### **Key Rules (in `/resources/rules/`)**  
1. **OrderProcessingRules.drl** – Applies discounts, sets priority.  
2. **DiscountRules.drl** – Calculates loyalty-based discounts.  
3. **CustomerValidationRules.drl** – Validates customer eligibility.  

---

## **File-Based Processing**  
- **Input**: Files placed in `input/orders/` (JSON format).  
- **Output**: Processed orders saved in `output/processed-orders/`.  

Example workflow:  
1. Drop `order.json` in `input/orders/`.  
2. Camel picks it up, processes via Drools.  
3. Result saved in `output/processed-orders/`.  

---

## **Error Handling**  
- **REST API Errors**: Returns structured JSON:  
  ```json
  { "error": "Processing failed", "message": "Invalid customer data" }
  ```
- **Drools Errors**: Logged, propagated as exceptions.  

---

## **How to Run**  
1. **Build & Run**:  
   ```sh
   mvn spring-boot:run
   ```
2. **Test APIs**:  
   - Use `POST /api/orders/process` for order submission.  
   - Use `GET /api/orders/sample` for a test payload.  
3. **File Processing**:  
   - Place JSON files in `input/orders/` and check `output/processed-orders/`.  

---

## **Dependencies**  
- **Apache Camel** (`camel-spring-boot-starter`)  
- **Drools** (`kie-spring`)  
- **Jackson** (`jackson-datatype-jsr310`)  

---

## **Future Improvements**  
🔹 **Add Kafka integration** for event-driven processing.  
🔹 **Extend rules** for fraud detection.  
🔹 **Add Swagger/OpenAPI** for API documentation.  

---

### **Conclusion**  
This system efficiently processes orders using **Camel routing** and **Drools rules**, providing:  
✔ **Flexibility** (rules can be modified without code changes)  
✔ **Scalability** (Camel supports multiple input sources)  
✔ **Maintainability** (clear separation of concerns)  

🚀 **Happy Processing!** 🚀
