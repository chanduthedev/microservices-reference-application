package com.anitechcs.orderservice.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.openapitools.jackson.nullable.JsonNullable;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * OrderErrorResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen")
public class OrderErrorResponse   {
  @JsonProperty("statusCode")
  private Integer statusCode;

  @JsonProperty("message")
  private String message;

  public OrderErrorResponse statusCode(Integer statusCode) {
    this.statusCode = statusCode;
    return this;
  }

  /**
   * Non zero error code
   * @return statusCode
  */
  @ApiModelProperty(value = "Non zero error code")


  public Integer getStatusCode() {
    return statusCode;
  }

  public void setStatusCode(Integer statusCode) {
    this.statusCode = statusCode;
  }

  public OrderErrorResponse message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Error message
   * @return message
  */
  @ApiModelProperty(value = "Error message")


  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderErrorResponse orderErrorResponse = (OrderErrorResponse) o;
    return Objects.equals(this.statusCode, orderErrorResponse.statusCode) &&
        Objects.equals(this.message, orderErrorResponse.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(statusCode, message);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderErrorResponse {\n");
    
    sb.append("    statusCode: ").append(toIndentedString(statusCode)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

