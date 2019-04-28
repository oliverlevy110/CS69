// Generated by gencpp from file levy_cs69_a2/Signal.msg
// DO NOT EDIT!


#ifndef LEVY_CS69_A2_MESSAGE_SIGNAL_H
#define LEVY_CS69_A2_MESSAGE_SIGNAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace levy_cs69_a2
{
template <class ContainerAllocator>
struct Signal_
{
  typedef Signal_<ContainerAllocator> Type;

  Signal_()
    : timestamp()
    , frame_id()
    , signal_strength(0.0)  {
    }
  Signal_(const ContainerAllocator& _alloc)
    : timestamp()
    , frame_id(_alloc)
    , signal_strength(0.0)  {
  (void)_alloc;
    }



   typedef ros::Time _timestamp_type;
  _timestamp_type timestamp;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _frame_id_type;
  _frame_id_type frame_id;

   typedef float _signal_strength_type;
  _signal_strength_type signal_strength;





  typedef boost::shared_ptr< ::levy_cs69_a2::Signal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::levy_cs69_a2::Signal_<ContainerAllocator> const> ConstPtr;

}; // struct Signal_

typedef ::levy_cs69_a2::Signal_<std::allocator<void> > Signal;

typedef boost::shared_ptr< ::levy_cs69_a2::Signal > SignalPtr;
typedef boost::shared_ptr< ::levy_cs69_a2::Signal const> SignalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::levy_cs69_a2::Signal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::levy_cs69_a2::Signal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace levy_cs69_a2

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'levy_cs69_a2': ['/home/oliverlevyorl/CS69/catkin_ws/src/levy_cs69_a2/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::levy_cs69_a2::Signal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::levy_cs69_a2::Signal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::levy_cs69_a2::Signal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::levy_cs69_a2::Signal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::levy_cs69_a2::Signal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::levy_cs69_a2::Signal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::levy_cs69_a2::Signal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb33c32f9c0ea1b07b6ab2b5c4362310";
  }

  static const char* value(const ::levy_cs69_a2::Signal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb33c32f9c0ea1b0ULL;
  static const uint64_t static_value2 = 0x7b6ab2b5c4362310ULL;
};

template<class ContainerAllocator>
struct DataType< ::levy_cs69_a2::Signal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "levy_cs69_a2/Signal";
  }

  static const char* value(const ::levy_cs69_a2::Signal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::levy_cs69_a2::Signal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "time timestamp\n\
string frame_id \n\
float32 signal_strength \n\
";
  }

  static const char* value(const ::levy_cs69_a2::Signal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::levy_cs69_a2::Signal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.timestamp);
      stream.next(m.frame_id);
      stream.next(m.signal_strength);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Signal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::levy_cs69_a2::Signal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::levy_cs69_a2::Signal_<ContainerAllocator>& v)
  {
    s << indent << "timestamp: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.timestamp);
    s << indent << "frame_id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.frame_id);
    s << indent << "signal_strength: ";
    Printer<float>::stream(s, indent + "  ", v.signal_strength);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LEVY_CS69_A2_MESSAGE_SIGNAL_H
