; Auto-generated. Do not edit!


(cl:in-package levy_cs69_a2-msg)


;//! \htmlinclude Signal.msg.html

(cl:defclass <Signal> (roslisp-msg-protocol:ros-message)
  ((timestamp
    :reader timestamp
    :initarg :timestamp
    :type cl:real
    :initform 0)
   (frame_id
    :reader frame_id
    :initarg :frame_id
    :type cl:string
    :initform "")
   (signal_strength
    :reader signal_strength
    :initarg :signal_strength
    :type cl:float
    :initform 0.0))
)

(cl:defclass Signal (<Signal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Signal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Signal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name levy_cs69_a2-msg:<Signal> is deprecated: use levy_cs69_a2-msg:Signal instead.")))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <Signal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader levy_cs69_a2-msg:timestamp-val is deprecated.  Use levy_cs69_a2-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'frame_id-val :lambda-list '(m))
(cl:defmethod frame_id-val ((m <Signal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader levy_cs69_a2-msg:frame_id-val is deprecated.  Use levy_cs69_a2-msg:frame_id instead.")
  (frame_id m))

(cl:ensure-generic-function 'signal_strength-val :lambda-list '(m))
(cl:defmethod signal_strength-val ((m <Signal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader levy_cs69_a2-msg:signal_strength-val is deprecated.  Use levy_cs69_a2-msg:signal_strength instead.")
  (signal_strength m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Signal>) ostream)
  "Serializes a message object of type '<Signal>"
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'timestamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'timestamp) (cl:floor (cl:slot-value msg 'timestamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'frame_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'frame_id))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'signal_strength))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Signal>) istream)
  "Deserializes a message object of type '<Signal>"
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'timestamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'frame_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'frame_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'signal_strength) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Signal>)))
  "Returns string type for a message object of type '<Signal>"
  "levy_cs69_a2/Signal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Signal)))
  "Returns string type for a message object of type 'Signal"
  "levy_cs69_a2/Signal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Signal>)))
  "Returns md5sum for a message object of type '<Signal>"
  "eb33c32f9c0ea1b07b6ab2b5c4362310")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Signal)))
  "Returns md5sum for a message object of type 'Signal"
  "eb33c32f9c0ea1b07b6ab2b5c4362310")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Signal>)))
  "Returns full string definition for message of type '<Signal>"
  (cl:format cl:nil "time timestamp~%string frame_id ~%float32 signal_strength ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Signal)))
  "Returns full string definition for message of type 'Signal"
  (cl:format cl:nil "time timestamp~%string frame_id ~%float32 signal_strength ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Signal>))
  (cl:+ 0
     8
     4 (cl:length (cl:slot-value msg 'frame_id))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Signal>))
  "Converts a ROS message object to a list"
  (cl:list 'Signal
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':frame_id (frame_id msg))
    (cl:cons ':signal_strength (signal_strength msg))
))
