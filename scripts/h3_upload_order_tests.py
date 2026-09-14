"""Offline fixtures; creates no media and makes no network requests."""
from pathlib import Path
import tempfile
import unittest
from h3_upload_order_lint import lint

class UploadOrderTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        # Existence fixtures only, deliberately not presented as rendered images/audio.
        (self.root/'face.png').write_bytes(b'fixture')
        (self.root/'voice.wav').write_bytes(b'fixture')
        self.image='<li data-upload-kind="image" data-slot="1" data-filename="face.png" data-role="角色外貌服装"><b>图片 1</b><a href="face.png">face.png</a><span>角色外貌服装</span></li>'
        self.audio='<li data-upload-kind="audio" data-slot="1" data-filename="voice.wav" data-role="音色参考" data-target="角色甲" data-audio-mode="audio reference" data-model-label="&lt;Audio 1&gt;"><b>音频 1</b><a href="voice.wav">voice.wav</a><span>角色甲 · 音色参考 · 6s</span></li>'
        self.box='<section data-upload-unit="H3-001"><h3>本段上传顺序</h3><ol>'+self.image+self.audio+'</ol></section>'
        self.prompt='<pre class="prompt-block">prompt fixture</pre>'

    def tearDown(self):self.tmp.cleanup()
    def check(self,content,passes=False):
        f=self.root/'page.html';f.write_text('<article class="h3-unit" data-h3-unit="H3-001">'+content+'</article>',encoding='utf-8')
        self.assertEqual(not lint(f),passes,lint(f))

    def test_valid(self):self.check(self.box+self.prompt,True)
    def test_missing_checklist(self):self.check(self.prompt)
    def test_wrong_unit(self):self.check(self.box.replace('H3-001','H3-002')+self.prompt)
    def test_collapsed(self):self.check('<details>'+self.box+'</details>'+self.prompt)
    def test_hidden(self):self.check(self.box.replace('<section ','<section hidden ')+self.prompt)
    def test_after_prompt(self):self.check(self.prompt+self.box)
    def test_skipped_slot(self):self.check(self.box.replace('data-slot="1"','data-slot="2"',1)+self.prompt)
    def test_duplicate_slot(self):self.check(self.box.replace(self.image,self.image*2)+self.prompt)
    def test_wrong_audio_label(self):self.check(self.box.replace('&lt;Audio 1&gt;','&lt;Audio 2&gt;')+self.prompt)
    def test_missing_audio_target(self):self.check(self.box.replace('data-target="角色甲"','')+self.prompt)
    def test_hidden_role(self):self.check(self.box.replace('<span>角色外貌服装</span>','')+self.prompt)
    def test_broken_link(self):self.check(self.box.replace('href="face.png"','href="absent.png"')+self.prompt)
    def test_data_uri_is_not_upload_file(self):self.check(self.box.replace('href="face.png"','href="data:image/png;base64,AAAA"')+self.prompt)
    def test_image_only(self):self.check(self.box.replace(self.audio,'')+self.prompt,True)
    def test_empty_requires_reason(self):self.check(self.box.replace(self.image,'').replace(self.audio,'')+self.prompt)
    def test_explicit_empty_mode(self):
        self.check('<section data-upload-unit="H3-001" data-no-visual-inputs="已明确文生模式">已明确文生模式</section>'+self.prompt,True)

if __name__=='__main__':unittest.main()
