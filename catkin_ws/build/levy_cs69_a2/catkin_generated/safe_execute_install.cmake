execute_process(COMMAND "/home/oliverlevyorl/CS69/catkin_ws/build/levy_cs69_a2/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/oliverlevyorl/CS69/catkin_ws/build/levy_cs69_a2/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
