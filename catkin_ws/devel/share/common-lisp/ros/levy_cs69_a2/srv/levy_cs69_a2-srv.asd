
(cl:in-package :asdf)

(defsystem "levy_cs69_a2-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FindSignalStrength" :depends-on ("_package_FindSignalStrength"))
    (:file "_package_FindSignalStrength" :depends-on ("_package"))
  ))