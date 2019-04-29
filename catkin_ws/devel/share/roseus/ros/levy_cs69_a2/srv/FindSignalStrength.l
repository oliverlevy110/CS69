;; Auto-generated. Do not edit!


(when (boundp 'levy_cs69_a2::FindSignalStrength)
  (if (not (find-package "LEVY_CS69_A2"))
    (make-package "LEVY_CS69_A2"))
  (shadow 'FindSignalStrength (find-package "LEVY_CS69_A2")))
(unless (find-package "LEVY_CS69_A2::FINDSIGNALSTRENGTH")
  (make-package "LEVY_CS69_A2::FINDSIGNALSTRENGTH"))
(unless (find-package "LEVY_CS69_A2::FINDSIGNALSTRENGTHREQUEST")
  (make-package "LEVY_CS69_A2::FINDSIGNALSTRENGTHREQUEST"))
(unless (find-package "LEVY_CS69_A2::FINDSIGNALSTRENGTHRESPONSE")
  (make-package "LEVY_CS69_A2::FINDSIGNALSTRENGTHRESPONSE"))

(in-package "ROS")





(defclass levy_cs69_a2::FindSignalStrengthRequest
  :super ros::object
  :slots (_x _y _theta ))

(defmethod levy_cs69_a2::FindSignalStrengthRequest
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:theta __theta) 0.0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _theta (float __theta))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:serialization-length
   ()
   (+
    ;; int32 _x
    4
    ;; int32 _y
    4
    ;; float32 _theta
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _x
       (write-long _x s)
     ;; int32 _y
       (write-long _y s)
     ;; float32 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _theta
     (setq _theta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass levy_cs69_a2::FindSignalStrengthResponse
  :super ros::object
  :slots (_avg_str ))

(defmethod levy_cs69_a2::FindSignalStrengthResponse
  (:init
   (&key
    ((:avg_str __avg_str) 0.0)
    )
   (send-super :init)
   (setq _avg_str (float __avg_str))
   self)
  (:avg_str
   (&optional __avg_str)
   (if __avg_str (setq _avg_str __avg_str)) _avg_str)
  (:serialization-length
   ()
   (+
    ;; float32 _avg_str
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _avg_str
       (sys::poke _avg_str (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _avg_str
     (setq _avg_str (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass levy_cs69_a2::FindSignalStrength
  :super ros::object
  :slots ())

(setf (get levy_cs69_a2::FindSignalStrength :md5sum-) "ab39b3c90f03c54cfc232becf20d8a15")
(setf (get levy_cs69_a2::FindSignalStrength :datatype-) "levy_cs69_a2/FindSignalStrength")
(setf (get levy_cs69_a2::FindSignalStrength :request) levy_cs69_a2::FindSignalStrengthRequest)
(setf (get levy_cs69_a2::FindSignalStrength :response) levy_cs69_a2::FindSignalStrengthResponse)

(defmethod levy_cs69_a2::FindSignalStrengthRequest
  (:response () (instance levy_cs69_a2::FindSignalStrengthResponse :init)))

(setf (get levy_cs69_a2::FindSignalStrengthRequest :md5sum-) "ab39b3c90f03c54cfc232becf20d8a15")
(setf (get levy_cs69_a2::FindSignalStrengthRequest :datatype-) "levy_cs69_a2/FindSignalStrengthRequest")
(setf (get levy_cs69_a2::FindSignalStrengthRequest :definition-)
      "int32 x
int32 y
float32 theta
---
float32 avg_str

")

(setf (get levy_cs69_a2::FindSignalStrengthResponse :md5sum-) "ab39b3c90f03c54cfc232becf20d8a15")
(setf (get levy_cs69_a2::FindSignalStrengthResponse :datatype-) "levy_cs69_a2/FindSignalStrengthResponse")
(setf (get levy_cs69_a2::FindSignalStrengthResponse :definition-)
      "int32 x
int32 y
float32 theta
---
float32 avg_str

")



(provide :levy_cs69_a2/FindSignalStrength "ab39b3c90f03c54cfc232becf20d8a15")


