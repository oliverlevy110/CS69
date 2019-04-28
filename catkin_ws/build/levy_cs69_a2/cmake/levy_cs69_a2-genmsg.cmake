# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "levy_cs69_a2: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ilevy_cs69_a2:/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(levy_cs69_a2_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg" NAME_WE)
add_custom_target(_levy_cs69_a2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "levy_cs69_a2" "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(levy_cs69_a2
  "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/levy_cs69_a2
)

### Generating Services

### Generating Module File
_generate_module_cpp(levy_cs69_a2
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/levy_cs69_a2
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(levy_cs69_a2_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(levy_cs69_a2_generate_messages levy_cs69_a2_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg" NAME_WE)
add_dependencies(levy_cs69_a2_generate_messages_cpp _levy_cs69_a2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(levy_cs69_a2_gencpp)
add_dependencies(levy_cs69_a2_gencpp levy_cs69_a2_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS levy_cs69_a2_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(levy_cs69_a2
  "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/levy_cs69_a2
)

### Generating Services

### Generating Module File
_generate_module_eus(levy_cs69_a2
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/levy_cs69_a2
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(levy_cs69_a2_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(levy_cs69_a2_generate_messages levy_cs69_a2_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg" NAME_WE)
add_dependencies(levy_cs69_a2_generate_messages_eus _levy_cs69_a2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(levy_cs69_a2_geneus)
add_dependencies(levy_cs69_a2_geneus levy_cs69_a2_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS levy_cs69_a2_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(levy_cs69_a2
  "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/levy_cs69_a2
)

### Generating Services

### Generating Module File
_generate_module_lisp(levy_cs69_a2
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/levy_cs69_a2
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(levy_cs69_a2_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(levy_cs69_a2_generate_messages levy_cs69_a2_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg" NAME_WE)
add_dependencies(levy_cs69_a2_generate_messages_lisp _levy_cs69_a2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(levy_cs69_a2_genlisp)
add_dependencies(levy_cs69_a2_genlisp levy_cs69_a2_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS levy_cs69_a2_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(levy_cs69_a2
  "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/levy_cs69_a2
)

### Generating Services

### Generating Module File
_generate_module_nodejs(levy_cs69_a2
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/levy_cs69_a2
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(levy_cs69_a2_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(levy_cs69_a2_generate_messages levy_cs69_a2_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg" NAME_WE)
add_dependencies(levy_cs69_a2_generate_messages_nodejs _levy_cs69_a2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(levy_cs69_a2_gennodejs)
add_dependencies(levy_cs69_a2_gennodejs levy_cs69_a2_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS levy_cs69_a2_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(levy_cs69_a2
  "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/levy_cs69_a2
)

### Generating Services

### Generating Module File
_generate_module_py(levy_cs69_a2
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/levy_cs69_a2
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(levy_cs69_a2_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(levy_cs69_a2_generate_messages levy_cs69_a2_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg/Signal.msg" NAME_WE)
add_dependencies(levy_cs69_a2_generate_messages_py _levy_cs69_a2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(levy_cs69_a2_genpy)
add_dependencies(levy_cs69_a2_genpy levy_cs69_a2_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS levy_cs69_a2_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/levy_cs69_a2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/levy_cs69_a2
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(levy_cs69_a2_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/levy_cs69_a2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/levy_cs69_a2
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(levy_cs69_a2_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/levy_cs69_a2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/levy_cs69_a2
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(levy_cs69_a2_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/levy_cs69_a2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/levy_cs69_a2
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(levy_cs69_a2_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/levy_cs69_a2)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/levy_cs69_a2\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/levy_cs69_a2
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/levy_cs69_a2
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/levy_cs69_a2/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(levy_cs69_a2_generate_messages_py std_msgs_generate_messages_py)
endif()
