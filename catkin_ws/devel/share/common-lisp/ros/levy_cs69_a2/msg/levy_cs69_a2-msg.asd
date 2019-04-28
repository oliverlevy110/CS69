
(cl:in-package :asdf)

(defsystem "levy_cs69_a2-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Signal" :depends-on ("_package_Signal"))
    (:file "_package_Signal" :depends-on ("_package"))
  ))