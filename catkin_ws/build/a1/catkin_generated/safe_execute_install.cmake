execute_process(COMMAND "/home/oliverlevyorl/CS69/catkin_ws/build/a1/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/oliverlevyorl/CS69/catkin_ws/build/a1/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
