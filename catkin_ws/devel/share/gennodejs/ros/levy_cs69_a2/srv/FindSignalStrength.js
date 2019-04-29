// Auto-generated. Do not edit!

// (in-package levy_cs69_a2.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class FindSignalStrengthRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.theta = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0;
      }
      if (initObj.hasOwnProperty('theta')) {
        this.theta = initObj.theta
      }
      else {
        this.theta = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FindSignalStrengthRequest
    // Serialize message field [x]
    bufferOffset = _serializer.int32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.int32(obj.y, buffer, bufferOffset);
    // Serialize message field [theta]
    bufferOffset = _serializer.float32(obj.theta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FindSignalStrengthRequest
    let len;
    let data = new FindSignalStrengthRequest(null);
    // Deserialize message field [x]
    data.x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [theta]
    data.theta = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'levy_cs69_a2/FindSignalStrengthRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1bbb9d09174792dc6528bb56a3b8cac1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 x
    int32 y
    float32 theta
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FindSignalStrengthRequest(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0
    }

    if (msg.theta !== undefined) {
      resolved.theta = msg.theta;
    }
    else {
      resolved.theta = 0.0
    }

    return resolved;
    }
};

class FindSignalStrengthResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.avg_str = null;
    }
    else {
      if (initObj.hasOwnProperty('avg_str')) {
        this.avg_str = initObj.avg_str
      }
      else {
        this.avg_str = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FindSignalStrengthResponse
    // Serialize message field [avg_str]
    bufferOffset = _serializer.float32(obj.avg_str, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FindSignalStrengthResponse
    let len;
    let data = new FindSignalStrengthResponse(null);
    // Deserialize message field [avg_str]
    data.avg_str = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'levy_cs69_a2/FindSignalStrengthResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '31fcbdc1bed5689fa5a0dc9cac81c933';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 avg_str
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FindSignalStrengthResponse(null);
    if (msg.avg_str !== undefined) {
      resolved.avg_str = msg.avg_str;
    }
    else {
      resolved.avg_str = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: FindSignalStrengthRequest,
  Response: FindSignalStrengthResponse,
  md5sum() { return 'ab39b3c90f03c54cfc232becf20d8a15'; },
  datatype() { return 'levy_cs69_a2/FindSignalStrength'; }
};
