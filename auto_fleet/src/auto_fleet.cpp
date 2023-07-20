#include <cstdio>
#include <chrono>

#include "rclcpp/rclcpp.hpp"
#include "rmf_fleet_msgs/msg/destination_request.hpp"

using namespace std::chrono_literals;

/*
class auto_free_fleet : public rclcpp::Node{
  public:
  auto_free_fleet():Node("auto_free_fleet"), cout_(0)
  {


  }
  private:
    rclcpp::TimerBase::SharedPtr timer_;

    rclcpp::Publisher<rmf_fleet_msgs::msg::DestinationRequest>::SharedPtr publisher_;
    rmf_fleet_msgs::msg::DestinationRequest Des_Request;

    char location;
}
*/
int i=0;

int main(int argc, char ** argv)
{
  printf("This programme aim to use free fleet\n");
  printf("author:lagrange.l\n");

  rclcpp::init(argc, argv);
  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("auto_ff_node");
  
  rclcpp::Publisher<rmf_fleet_msgs::msg::DestinationRequest>::SharedPtr publisher_;
  publisher_ = node->create_publisher<rmf_fleet_msgs::msg::DestinationRequest>("robot_destination_requests", 10);

  rmf_fleet_msgs::msg::DestinationRequest Des_Request_1;
  rmf_fleet_msgs::msg::DestinationRequest Des_Request_2;
  rmf_fleet_msgs::msg::DestinationRequest Des_Request_3;


  Des_Request_1.fleet_name="turtlebot3";
  Des_Request_1.robot_name="tb3_0";
  Des_Request_1.destination.t.sec=100;
  Des_Request_1.destination.t.nanosec=100;
  Des_Request_1.destination.x=10;
  Des_Request_1.destination.y=10;
  Des_Request_1.destination.yaw=0;
  Des_Request_1.destination.level_name="house";
  Des_Request_1.task_id='1';


  Des_Request_2.fleet_name="turtlebot3";
  Des_Request_2.robot_name="tb3_1";
  Des_Request_2.destination.t.sec=100;
  Des_Request_2.destination.t.nanosec=100;
  Des_Request_2.destination.x=9;
  Des_Request_2.destination.y=9;
  Des_Request_2.destination.yaw=0;
  Des_Request_2.destination.level_name="house";
  Des_Request_2.task_id='2';



  Des_Request_3.fleet_name="turtlebot3";
  Des_Request_3.robot_name="tb3_2";
  Des_Request_3.destination.t.sec=100;
  Des_Request_3.destination.t.nanosec=100;
  Des_Request_3.destination.x=10;
  Des_Request_3.destination.y=-1;
  Des_Request_3.destination.yaw=0;
  Des_Request_3.destination.level_name="house";
  Des_Request_3.task_id='3';

for(i=0;i<100000;i++)
{
  publisher_->publish(Des_Request_1);
  publisher_->publish(Des_Request_2);
  publisher_->publish(Des_Request_3);
}
   // }
  //rclcpp::spin(std::make_shared<MinimalPublisher>());
  //rclcpp::shutdown();
  return 0;
}
