from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hri_audio_stack',
            executable='voice_speaker_action_server',
            name='audio_stack_speak',
            output='screen'
        ),
    ])