import argparse
def options():
    
    
    parser = argparse.ArgumentParser(description='Inference code to lip-sync videos in the wild using Wav2Lip models')
    
    #Arguments for tortoise
    
    parser.add_argument('--text', type=str, help='Text to speak.', default="The expressiveness of autoregressive transformers is literally nuts! I absolutely adore them.")
    parser.add_argument('--voice', type=str, help='Selects the voice to use for generation. See options in voices/ directory (and add your own!) '
                                                 'Use the & character to join two voices together. Use a comma to perform inference on multiple voices.', default='tom')
    parser.add_argument('--preset', type=str, help='Which voice preset to use.', default='fast')
    parser.add_argument('--output_path', type=str, help='Where to store outputs.', default='results/')
    parser.add_argument('--model_dir', type=str, help='Where to find pretrained model checkpoints. Tortoise automatically downloads these to .models, so this'
                                                      'should only be specified if you have custom checkpoints.', default='/root/.cache/tortoise/models')
    parser.add_argument('--candidates', type=int, help='How many output candidates to produce per-voice.', default=1)
    parser.add_argument('--seed', type=int, help='Random seed which can be used to reproduce results.', default=None)
    parser.add_argument('--produce_debug_state', type=bool, help='Whether or not to produce debug_state.pth, which can aid in reproducing problems. Defaults to true.', default=True)
    parser.add_argument('--cvvp_amount', type=float, help='How much the CVVP model should influence the output.'
                                                          'Increasing this can in some cases reduce the likelihood of multiple speakers. Defaults to 0 (disabled)', default=.0)
    
    #arguments for wav2lip
    # parser = argparse.ArgumentParser(description='Inference code to lip-sync videos in the wild using Wav2Lip models')

    parser.add_argument('--checkpoint_path', type=str,
              help='Name of saved checkpoint to load weights from', default='Wav2Lip/checkpoints/wav2lip_gan.pth')

    parser.add_argument('--face', type=str,
              help='Filepath of video/image that contains faces to use', required=True)
    parser.add_argument('--audio', type=str,
              help='Filepath of video/audio file to use as raw audio source', default='/content/drive/MyDrive/any2English/results/tom_0.wav')
    parser.add_argument('--outfile', type=str, help='Video path to save result. See default for an e.g.',
                    default='results/result_voice.mp4')

    parser.add_argument('--static', type=bool,
              help='If True, then use only first video frame for inference', default=False)
    parser.add_argument('--fps', type=float, help='Can be specified only if input is a static image (default: 25)',
              default=25., required=False)

    parser.add_argument('--pads', nargs='+', type=int, default=[0, 10, 0, 0],
              help='Padding (top, bottom, left, right). Please adjust to include chin at least')

    parser.add_argument('--face_det_batch_size', type=int,
              help='Batch size for face detection', default=16)
    parser.add_argument('--wav2lip_batch_size', type=int, help='Batch size for Wav2Lip model(s)', default=128)

    parser.add_argument('--resize_factor', default=1, type=int,
          help='Reduce the resolution by this factor. Sometimes, best results are obtained at 480p or 720p')

    parser.add_argument('--crop', nargs='+', type=int, default=[0, -1, 0, -1],
              help='Crop video to a smaller region (top, bottom, left, right). Applied after resize_factor and rotate arg. '
              'Useful if multiple face present. -1 implies the value will be auto-inferred based on height, width')

    parser.add_argument('--box', nargs='+', type=int, default=[-1, -1, -1, -1],
              help='Specify a constant bounding box for the face. Use only as a last resort if the face is not detected.'
              'Also, might work only if the face is not moving around much. Syntax: (top, bottom, left, right).')

    parser.add_argument('--rotate', default=False, action='store_true',
              help='Sometimes videos taken from a phone can be flipped 90deg. If true, will flip video right by 90deg.'
              'Use if you get a flipped result, despite feeding a normal looking video')

    parser.add_argument('--nosmooth', default=False, action='store_true',
              help='Prevent smoothing face detections over a short temporal window')

    args = parser.parse_args()
    return args