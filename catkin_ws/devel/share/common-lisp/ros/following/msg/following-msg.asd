
(cl:in-package :asdf)

(defsystem "following-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Signal" :depends-on ("_package_Signal"))
    (:file "_package_Signal" :depends-on ("_package"))
  ))