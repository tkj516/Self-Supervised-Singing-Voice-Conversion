import os

BASE = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
  <meta charset="UTF-8">
  <title align="center">Audio samples for "SELF-SUPERVISED REPRESENTATIONS FOR SINGING VOICE SYNTHESIS"</title>
  <style type="text/css">
    body,
    input,
    select,
    td,
    li,
    div,
    textarea,
    p {
      font-size: 11px;
      line-height: 16px;
      font-family: verdana, arial, sans-serif;
    }

    body {
      margin: 5px;
      background-color: white;
    }

    h1 {
      font-size: 16px;
      font-weight: bold;
    }

    h2 {
      font-size: 14px;
      font-weight: bold;
    }
  </style>
</head>

<body>
  <article>
    <header>
      <h1>Audio samples for "SELF-SUPERVISED REPRESENTATIONS FOR SINGING VOICE SYNTHESIS"</h1>
    </header>
  </article>

  <!--       <div>
      PAPER accepted by INTERSPEECH 2020: <a href = https://arxiv.org/abs/2002.06758 >pdf</a>
      </div> -->

  <!--       <div>
      Website license info sheet <a href = https://yolanda-gao.github.io/Interactive-Style-TTS/Interactive_TTS_license.pdf >pdf</a>
      </div> -->


  <div>
    <h2>Abstract</h2>
    <p>A singing voice conversion model converts a song in the voice of an arbitrary source singer to the voice of a
      target singer. Recently, methods that leverage self-supervised audio representations suchas HuBERT and Wav2Vec 2.0 
      have helped further the state-of-the-art. Though these methods produce more natural and melodic singing outputs, 
      they often rely on confusion and disentanglement losses to render the self-supervised representations speaker and 
      pitch-invariant. In this paper, we circumvent disentanglement training and propose a new model that leverages ASR 
      fine-tuned self-supervised representations as inputs to a HiFi-GAN neural vocoder for singing voice conversion. We
      experiment with different f0 encoding schemes and show that an f0 harmonic generation module that uses a parallel
      bank of transposed convolutions (PBTC) alongside ASR fine-tuned Wav2Vec 2.0 features results in the best singing voice 
      conversion quality. Additionally, the model is capable of making a spoken voice sing. We also show that a simple f0 
      shifting scheme during inference helps retain singer identity and bolsters the performance of our singing voice conversion 
      model. Our results are backed up by extensive MOS studies that compare different ablations and baselines.</p>
  </div>

  <h2> Contents </h2>
  <div id="toc_container">
    <ul>
      <b> <a href="#MOS1">A: MOS Study 1 samples</a> </b><br />
      <b> <a href="#MOS2">B: MOS Study 2 Samples </a> </b><br />
      <b> <a href="#MOS3">C: MOS Study 3 Samples</a> </b><br />
      <b> <a href="#MOS4">D: MOS Study 4 Samples</a> </b><br />
    </ul>
  </div>
"""

SECTION_TEMPLATE="""
  <div>
  </div>
  <!---    <h1>Samples for six styles</h1> -->
  <h1> {section_name} </h1>
  <p><a id='{section_id}'></a></p>
  <p> {section_abstract}
  </p>

  <div>
    <h2> {section_header} </h2>
    <table border="1" class="inlineTable">
      {section_table}
    </table>
  </div>
"""

CELL_TEMPLATE="""
        <td>
          <audio controls style="width: 200px;">
            <source src={src} type="audio/wav">
            Your browser does not support the audio element.
          </audio>
        </td>
"""

END = """
    </table>
  </div>

</body>

</html>
"""

MAP = {
      "03_00017000_00034200.mastered.wav": "monologue_a0048.mastered.wav",
      "04_00058000_00074500.mastered.wav": "base_c_06880.mastered.wav",
      "06_00096000_00112500.mastered.wav": "base_a_08925.mastered.wav",
      "07_00045500_00062000.mastered.wav": "base_a_05118.mastered.wav",
      "11_00099000_00115500.mastered.wav": "base_c_06698.mastered.wav",
      "12_00002700_00019200.mastered.wav": "monologue_a0052.mastered.wav",
      "15_00018000_00034500.mastered.wav": "base_c_09581.mastered.wav",
      "15_00086100_00102700.mastered.wav": "monologue_a0072.mastered.wav",
      "18_00003400_00019900.mastered.wav": "base_c_09219.mastered.wav",
      "18_00043200_00059900.mastered.wav": "base_a_08764.mastered.wav",
      "18_00181300_00197800.mastered.wav": "monologue_a0065.mastered.wav",
      "20_00049900_00066400.mastered.wav": "base_c_04955.mastered.wav",
      "F08023019.mastered.wav": "base_c_06645.mastered.wav",
      "M04025017.mastered.wav": "base_a_09093.mastered.wav",
      "en027b_00065200_00076930.mastered.wav": "base_c_06903.mastered.wav",
      "en032b_00048800_00060260.mastered.wav": "base_c_11350.mastered.wav",
}

def generate_table(
    root_dir: str,
):
    experiments = os.listdir(root_dir)
    table = ""
    reference_cache_filled = False
    reference_cache = []
    for experiment in experiments:
        if experiment == ".DS_Store":
            continue
        table += """
            <tr>
                <th width="200">{experiment}</th>
        """.format(experiment=experiment)
        for sample in sorted(os.listdir(os.path.join(root_dir, experiment))):
            if experiment == "reference":
                sample = MAP[reference_cache.pop(0)]
            table += CELL_TEMPLATE.format(
                src=os.path.join(root_dir, experiment, sample)
            )
            if "reference" in experiments and not reference_cache_filled:
                reference_cache.append(sample)
        table += """
            </tr>
        """
        reference_cache_filled = True

    return table

if __name__ == "__main__":
    html = BASE

    table_a = generate_table("MOS1")
    abstract_a ="""
        Samples from MOS Study 1.  Raters were asked the judge the audio quality
        across different models.  Each model uses HuBERT as the self-supervised
        feature, but varies the training procedure (e.g., using only singing data
        vs. singing + spoken speech data) or varies the f0 feature encoder (e.g.,
        PBTC vs. Q-LUT).
    """
    section_a = SECTION_TEMPLATE.format(
        section_name="Section A",
        section_id="MOS1",
        section_abstract=abstract_a,
        section_header="Comparing different models with HuBERT self-supervised features",
        section_table=table_a,
    )
    html += section_a

    table_b = generate_table("MOS3")
    abstract_b ="""
        Samples from MOS Study 2.  Raters were asked to judge the speaker/singer
        similarity between the synthesized audio and the reference audio.
    """
    section_b = SECTION_TEMPLATE.format(
        section_name="Section B",
        section_id="MOS2",
        section_abstract=abstract_b,
        section_header="Target singer/speaker similarity with HuBERT self-supervised features",
        section_table=table_b,
    )
    html += section_b

    table_c = generate_table("MOS2")
    abstract_c ="""
        Samples from MOS Study 3.  Raters were asked the judge the audio quality
        across different models.  Each varies the self-supervised
        feature (HuBERT vsv Wav2Vec2.0 vs. Wav3Vec2.0-ASR), and also varies the 
        f0 feature encoder (e.g., PBTC vs. Q-LUT).
    """
    section_c = SECTION_TEMPLATE.format(
        section_name="Section C",
        section_id="MOS3",
        section_abstract=abstract_c,
        section_header="Comparing different models by varying self-supervised and f0 features",
        section_table=table_c,
    )
    html += section_c

    table_d = generate_table("MOS4")
    abstract_d ="""
        Samples from MOS Study 4.  Raters were asked to judge the speaker/singer
        similarity between the synthesized audio and the reference audio with 
        and without f0 shifting during inference.
    """
    section_d = SECTION_TEMPLATE.format(
        section_name="Section D",
        section_id="MOS4",
        section_abstract=abstract_d,
        section_header="Comparing Different Models with HuBERT Self-supervised Features",
        section_table=table_d,
    )
    html += section_d

    html += END

    with open("index.html", "w") as f:
        f.write(html)