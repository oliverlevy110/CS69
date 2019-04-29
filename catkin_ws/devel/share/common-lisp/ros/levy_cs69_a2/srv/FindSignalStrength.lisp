; Auto-generated. Do not edit!


(cl:in-package levy_cs69_a2-srv)


;//! \htmlinclude FindSignalStrength-request.msg.html

(cl:defclass <FindSignalStrength-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0)
   (theta
    :reader theta
    :initarg :theta
    :type cl:float
    :initform 0.0))
)

(cl:defclass FindSignalStrength-request (<FindSignalStrength-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FindSignalStrength-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FindSignalStrength-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name levy_cs69_a2-srv:<FindSignalStrength-request> is deprecated: use levy_cs69_a2-srv:FindSignalStrength-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <FindSignalStrength-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader levy_cs69_a2-srv:x-val is deprecated.  Use levy_cs69_a2-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <FindSignalStrength-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader levy_cs69_a2-srv:y-val is deprecated.  Use levy_cs69_a2-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'theta-val :lambda-list '(m))
(cl:defmethod theta-val ((m <FindSignalStrength-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader levy_cs69_a2-srv:theta-val is deprecated.  Use levy_cs69_a2-srv:theta instead.")
  (theta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FindSignalStrength-request>) ostream)
  "Serializes a message object of type '<FindSignalStrength-request>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FindSignalStrength-request>) istream)
  "Deserializes a message object of type '<FindSignalStrength-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FindSignalStrength-request>)))
  "Returns string type for a service object of type '<FindSignalStrength-request>"
  "levy_cs69_a2/FindSignalStrengthRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FindSignalStrength-request)))
  "Returns string type for a service object of type 'FindSignalStrength-request"
  "levy_cs69_a2/FindSignalStrengthRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FindSignalStrength-request>)))
  "Returns md5sum for a message object of type '<FindSignalStrength-request>"
  "ab39b3c90f03c54cfc232becf20d8a15")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FindSignalStrength-request)))
  "Returns md5sum for a message object of type 'FindSignalStrength-request"
  "ab39b3c90f03c54cfc232becf20d8a15")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FindSignalStrength-request>)))
  "Returns full string definition for message of type '<FindSignalStrength-request>"
  (cl:format cl:nil "int32 x~%int32 y~%float32 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FindSignalStrength-request)))
  "Returns full string definition for message of type 'FindSignalStrength-request"
  (cl:format cl:nil "int32 x~%int32 y~%float32 theta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FindSignalStrength-request>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FindSignalStrength-request>))
  "Converts a ROS message object to a list"
  (cl:list 'FindSignalStrength-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':theta (theta msg))
))
;//! \htmlinclude FindSignalStrength-response.msg.html

(cl:defclass <FindSignalStrength-response> (roslisp-msg-protocol:ros-message)
  ((avg_str
    :reader avg_str
    :initarg :avg_str
    :type cl:float
    :initform 0.0))
)

(cl:defclass FindSignalStrength-response (<FindSignalStrength-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FindSignalStrength-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FindSignalStrength-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name levy_cs69_a2-srv:<FindSignalStrength-response> is deprecated: use levy_cs69_a2-srv:FindSignalStrength-response instead.")))

(cl:ensure-generic-function 'avg_str-val :lambda-list '(m))
(cl:defmethod avg_str-val ((m <FindSignalStrength-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader levy_cs69_a2-srv:avg_str-val is deprecated.  Use levy_cs69_a2-srv:avg_str instead.")
  (avg_str m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FindSignalStrength-response>) ostream)
  "Serializes a message object of type '<FindSignalStrength-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'avg_str))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FindSignalStrength-response>) istream)
  "Deserializes a message object of type '<FindSignalStrength-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'avg_str) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FindSignalStrength-response>)))
  "Returns string type for a service object of type '<FindSignalStrength-response>"
  "levy_cs69_a2/FindSignalStrengthResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FindSignalStrength-response)))
  "Returns string type for a service object of type 'FindSignalStrength-response"
  "levy_cs69_a2/FindSignalStrengthResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FindSignalStrength-response>)))
  "Returns md5sum for a message object of type '<FindSignalStrength-response>"
  "ab39b3c90f03c54cfc232becf20d8a15")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FindSignalStrength-response)))
  "Returns md5sum for a message object of type 'FindSignalStrength-response"
  "ab39b3c90f03c54cfc232becf20d8a15")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FindSignalStrength-response>)))
  "Returns full string definition for message of type '<FindSignalStrength-response>"
  (cl:format cl:nil "float32 avg_str~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FindSignalStrength-response)))
  "Returns full string definition for message of type 'FindSignalStrength-response"
  (cl:format cl:nil "float32 avg_str~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FindSignalStrength-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FindSignalStrength-response>))
  "Converts a ROS message object to a list"
  (cl:list 'FindSignalStrength-response
    (cl:cons ':avg_str (avg_str msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'FindSignalStrength)))
  'FindSignalStrength-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'FindSignalStrength)))
  'FindSignalStrength-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FindSignalStrength)))
  "Returns string type for a service object of type '<FindSignalStrength>"
  "levy_cs69_a2/FindSignalStrength")