;; Auto-generated. Do not edit!


(when (boundp 'levy_cs69_a2::Signal)
  (if (not (find-package "LEVY_CS69_A2"))
    (make-package "LEVY_CS69_A2"))
  (shadow 'Signal (find-package "LEVY_CS69_A2")))
(unless (find-package "LEVY_CS69_A2::SIGNAL")
  (make-package "LEVY_CS69_A2::SIGNAL"))

(in-package "ROS")
;;//! \htmlinclude Signal.msg.html


(defclass levy_cs69_a2::Signal
  :super ros::object
  :slots (_timestamp _frame_id _signal_strength ))

(defmethod levy_cs69_a2::Signal
  (:init
   (&key
    ((:timestamp __timestamp) (instance ros::time :init))
    ((:frame_id __frame_id) "")
    ((:signal_strength __signal_strength) 0.0)
    )
   (send-super :init)
   (setq _timestamp __timestamp)
   (setq _frame_id (string __frame_id))
   (setq _signal_strength (float __signal_strength))
   self)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:frame_id
   (&optional __frame_id)
   (if __frame_id (setq _frame_id __frame_id)) _frame_id)
  (:signal_strength
   (&optional __signal_strength)
   (if __signal_strength (setq _signal_strength __signal_strength)) _signal_strength)
  (:serialization-length
   ()
   (+
    ;; time _timestamp
    8
    ;; string _frame_id
    4 (length _frame_id)
    ;; float32 _signal_strength
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _timestamp
       (write-long (send _timestamp :sec) s) (write-long (send _timestamp :nsec) s)
     ;; string _frame_id
       (write-long (length _frame_id) s) (princ _frame_id s)
     ;; float32 _signal_strength
       (sys::poke _signal_strength (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _timestamp
     (send _timestamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _timestamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _frame_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _frame_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _signal_strength
     (setq _signal_strength (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get levy_cs69_a2::Signal :md5sum-) "eb33c32f9c0ea1b07b6ab2b5c4362310")
(setf (get levy_cs69_a2::Signal :datatype-) "levy_cs69_a2/Signal")
(setf (get levy_cs69_a2::Signal :definition-)
      "time timestamp
string frame_id 
float32 signal_strength 

")



(provide :levy_cs69_a2/Signal "eb33c32f9c0ea1b07b6ab2b5c4362310")


