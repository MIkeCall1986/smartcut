#!/usr/bin/env python3
"""
Real video file test for fetch_frame.
Takes a video file, opens it with MediaContainer, uses fetch_frame to count frames,
and compares with actual frame count.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from smartcut.media_container import MediaContainer
from smartcut.cut_video import VideoCutter, VideoSettings, VideoExportMode, VideoExportQuality
import av

def test_fetch_frame_with_real_video(video_path):
    """Test fetch_frame with a real video file"""
    print(f"Testing fetch_frame with: {video_path}")

    if not os.path.exists(video_path):
        print(f"❌ Video file not found: {video_path}")
        return False

    try:
        # Open media container
        print("Opening MediaContainer...")
        media_container = MediaContainer(video_path)

        if media_container.video_stream is None:
            print("❌ No video stream found")
            return False

        print(f"Video info:")
        print(f"  Duration: {float(media_container.duration()):.2f}s")
        print(f"  GOP count: {len(media_container.gop_start_times_dts)}")
        print(f"  Frame rate: {media_container.video_stream.guessed_rate}")

        # Get actual frame count from the video
        with av.open(video_path) as container:
            video_stream = container.streams.video[0]
            actual_frame_count = 0
            for frame in container.decode(video_stream):
                actual_frame_count += 1

        print(f"Actual frame count: {actual_frame_count}")

        # Create a dummy output container for VideoCutter
        output_container = av.open('dummy.mp4', 'w')

        try:
            # Create VideoCutter
            video_settings = VideoSettings(VideoExportMode.RECODE, VideoExportQuality.NORMAL, None)
            cutter = VideoCutter(media_container, output_container, video_settings, None)

            # Count frames using fetch_frame for each GOP
            total_fetched_frames = 0

            for i, (gop_start_dts, gop_end_dts) in enumerate(zip(
                media_container.gop_start_times_dts,
                media_container.gop_end_times_dts
            )):
                print(f"Processing GOP {i+1}/{len(media_container.gop_start_times_dts)}...")

                # Get all frames for this GOP with a large pts_end_time
                gop_frames = list(cutter.fetch_frame(gop_start_dts, gop_end_dts, 100_000_000))
                gop_frame_count = len(gop_frames)
                total_fetched_frames += gop_frame_count

                print(f"  GOP {i+1}: {gop_frame_count} frames")

            print(f"\nResults:")
            print(f"  Total fetched frames: {total_fetched_frames}")
            print(f"  Actual frame count: {actual_frame_count}")
            print(f"  Match: {'✅' if total_fetched_frames == actual_frame_count else '❌'}")

            success = total_fetched_frames == actual_frame_count

        finally:
            output_container.close()
            # Clean up dummy file
            if os.path.exists('dummy.mp4'):
                os.remove('dummy.mp4')

        return success

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_fetch_frame_real.py <video_file>")
        sys.exit(1)

    video_path = sys.argv[1]
    success = test_fetch_frame_with_real_video(video_path)

    if success:
        print("\n✅ Test PASSED: fetch_frame correctly processes all frames")
    else:
        print("\n❌ Test FAILED: Frame count mismatch")

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()