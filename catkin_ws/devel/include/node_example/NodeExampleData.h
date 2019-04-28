// Generated by gencpp from file node_example/NodeExampleData.msg
// DO NOT EDIT!


#ifndef NODE_EXAMPLE_MESSAGE_NODEEXAMPLEDATA_H
#define NODE_EXAMPLE_MESSAGE_NODEEXAMPLEDATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace node_example
{
template <class ContainerAllocator>
struct NodeExampleData_
{
  typedef NodeExampleData_<ContainerAllocator> Type;

  NodeExampleData_()
    : message()
    , a(0)
    , b(0)  {
    }
  NodeExampleData_(const ContainerAllocator& _alloc)
    : message(_alloc)
    , a(0)
    , b(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _message_type;
  _message_type message;

   typedef int32_t _a_type;
  _a_type a;

   typedef int32_t _b_type;
  _b_type b;





  typedef boost::shared_ptr< ::node_example::NodeExampleData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::node_example::NodeExampleData_<ContainerAllocator> const> ConstPtr;

}; // struct NodeExampleData_

typedef ::node_example::NodeExampleData_<std::allocator<void> > NodeExampleData;

typedef boost::shared_ptr< ::node_example::NodeExampleData > NodeExampleDataPtr;
typedef boost::shared_ptr< ::node_example::NodeExampleData const> NodeExampleDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::node_example::NodeExampleData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::node_example::NodeExampleData_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace node_example

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'node_example': ['/home/oliverlevyorl/CS69/catkin_ws/src/dynamicPubSubExample/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::node_example::NodeExampleData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::node_example::NodeExampleData_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::node_example::NodeExampleData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::node_example::NodeExampleData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::node_example::NodeExampleData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::node_example::NodeExampleData_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::node_example::NodeExampleData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3192b76bfe6df73dcca63fc0aa4efaf9";
  }

  static const char* value(const ::node_example::NodeExampleData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3192b76bfe6df73dULL;
  static const uint64_t static_value2 = 0xcca63fc0aa4efaf9ULL;
};

template<class ContainerAllocator>
struct DataType< ::node_example::NodeExampleData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "node_example/NodeExampleData";
  }

  static const char* value(const ::node_example::NodeExampleData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::node_example::NodeExampleData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string message\n\
int32 a\n\
int32 b\n\
";
  }

  static const char* value(const ::node_example::NodeExampleData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::node_example::NodeExampleData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.message);
      stream.next(m.a);
      stream.next(m.b);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct NodeExampleData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::node_example::NodeExampleData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::node_example::NodeExampleData_<ContainerAllocator>& v)
  {
    s << indent << "message: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.message);
    s << indent << "a: ";
    Printer<int32_t>::stream(s, indent + "  ", v.a);
    s << indent << "b: ";
    Printer<int32_t>::stream(s, indent + "  ", v.b);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NODE_EXAMPLE_MESSAGE_NODEEXAMPLEDATA_H