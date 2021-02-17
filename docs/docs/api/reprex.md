---
title: reprexlite.reprex
---
<div>

<style type="text/css">/*! pygments syntax highlighting */pre{line-height:125%;}td.linenos pre{color:#000000; background-color:#f0f0f0; padding-left:5px; padding-right:5px;}span.linenos{color:#000000; background-color:#f0f0f0; padding-left:5px; padding-right:5px;}td.linenos pre.special{color:#000000; background-color:#ffffc0; padding-left:5px; padding-right:5px;}span.linenos.special{color:#000000; background-color:#ffffc0; padding-left:5px; padding-right:5px;}.pdoc .hll{background-color:#ffffcc}.pdoc{background:#f8f8f8;}.pdoc .c{color:#408080; font-style:italic}.pdoc .err{border:1px solid #FF0000}.pdoc .k{color:#008000; font-weight:bold}.pdoc .o{color:#666666}.pdoc .ch{color:#408080; font-style:italic}.pdoc .cm{color:#408080; font-style:italic}.pdoc .cp{color:#BC7A00}.pdoc .cpf{color:#408080; font-style:italic}.pdoc .c1{color:#408080; font-style:italic}.pdoc .cs{color:#408080; font-style:italic}.pdoc .gd{color:#A00000}.pdoc .ge{font-style:italic}.pdoc .gr{color:#FF0000}.pdoc .gh{color:#000080; font-weight:bold}.pdoc .gi{color:#00A000}.pdoc .go{color:#888888}.pdoc .gp{color:#000080; font-weight:bold}.pdoc .gs{font-weight:bold}.pdoc .gu{color:#800080; font-weight:bold}.pdoc .gt{color:#0044DD}.pdoc .kc{color:#008000; font-weight:bold}.pdoc .kd{color:#008000; font-weight:bold}.pdoc .kn{color:#008000; font-weight:bold}.pdoc .kp{color:#008000}.pdoc .kr{color:#008000; font-weight:bold}.pdoc .kt{color:#B00040}.pdoc .m{color:#666666}.pdoc .s{color:#BA2121}.pdoc .na{color:#7D9029}.pdoc .nb{color:#008000}.pdoc .nc{color:#0000FF; font-weight:bold}.pdoc .no{color:#880000}.pdoc .nd{color:#AA22FF}.pdoc .ni{color:#999999; font-weight:bold}.pdoc .ne{color:#D2413A; font-weight:bold}.pdoc .nf{color:#0000FF}.pdoc .nl{color:#A0A000}.pdoc .nn{color:#0000FF; font-weight:bold}.pdoc .nt{color:#008000; font-weight:bold}.pdoc .nv{color:#19177C}.pdoc .ow{color:#AA22FF; font-weight:bold}.pdoc .w{color:#bbbbbb}.pdoc .mb{color:#666666}.pdoc .mf{color:#666666}.pdoc .mh{color:#666666}.pdoc .mi{color:#666666}.pdoc .mo{color:#666666}.pdoc .sa{color:#BA2121}.pdoc .sb{color:#BA2121}.pdoc .sc{color:#BA2121}.pdoc .dl{color:#BA2121}.pdoc .sd{color:#BA2121; font-style:italic}.pdoc .s2{color:#BA2121}.pdoc .se{color:#BB6622; font-weight:bold}.pdoc .sh{color:#BA2121}.pdoc .si{color:#BB6688; font-weight:bold}.pdoc .sx{color:#008000}.pdoc .sr{color:#BB6688}.pdoc .s1{color:#BA2121}.pdoc .ss{color:#19177C}.pdoc .bp{color:#008000}.pdoc .fm{color:#0000FF}.pdoc .vc{color:#19177C}.pdoc .vg{color:#19177C}.pdoc .vi{color:#19177C}.pdoc .vm{color:#19177C}.pdoc .il{color:#666666}</style>
<style type="text/css">/*! pdoc */:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f7f7f7;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}html, main{scroll-behavior:smooth;}.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3, .pdoc h4{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{background-color:var(--code);border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--code);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.pdoc details{--shift:-40px;text-align:right;margin-top:var(--shift);margin-bottom:calc(0px - var(--shift));clear:both;filter:opacity(1);}.pdoc details:not([open]){height:0;overflow:visible;}.pdoc details > summary{font-size:.75rem;cursor:pointer;color:var(--muted);border-width:0;padding:0 .7em;display:inline-block;display:inline list-item;user-select:none;}.pdoc details > summary:focus{outline:0;}.pdoc details > div{margin-top:calc(0px - var(--shift) / 2);text-align:left;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc > section:first-of-type > .docstring{margin-bottom:3rem;}.pdoc .docstring pre{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc .headerlink{position:absolute;width:0;margin-left:-1.5rem;line-height:1.4rem;font-size:1.5rem;font-weight:normal;transition:all 100ms ease-in-out;opacity:0;}.pdoc .attr > .headerlink{margin-left:-2.5rem;}.pdoc *:hover > .headerlink,.pdoc *:target > .attr > .headerlink{opacity:1;}.pdoc .attr{color:var(--text);margin:1rem 0 .5rem;padding:.4rem 5rem .4rem 1rem;background-color:var(--accent);}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{white-space:pre-wrap;}.pdoc .annotation{color:var(--annotation);}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}</style>    <main class="pdoc">
            <section>
                    <h1 class="modulename">
reprexlite.reprex    </h1>

                
                        <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="kn">from</span> <span class="nn">abc</span> <span class="kn">import</span> <span class="n">ABC</span><span class="p">,</span> <span class="n">abstractmethod</span>
<span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span>
<span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
<span class="kn">from</span> <span class="nn">pathlib</span> <span class="kn">import</span> <span class="n">Path</span>
<span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Optional</span>

<span class="kn">from</span> <span class="nn">reprexlite.code</span> <span class="kn">import</span> <span class="n">CodeBlock</span>
<span class="kn">from</span> <span class="nn">reprexlite.session_info</span> <span class="kn">import</span> <span class="n">SessionInfo</span>
<span class="kn">from</span> <span class="nn">reprexlite.version</span> <span class="kn">import</span> <span class="n">__version__</span>


<span class="k">class</span> <span class="nc">Advertisement</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class for generating the advertisement note for reprexlite.&quot;&quot;&quot;</span>

    <span class="n">pkg</span> <span class="o">=</span> <span class="s2">&quot;reprexlite&quot;</span>
    <span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;https://github.com/jayqi/reprexlite&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">now</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">astimezone</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S %Z&quot;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">created</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;Created at </span><span class="si">{</span><span class="n">now</span><span class="si">}</span><span class="s2"> by&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ver</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;v</span><span class="si">{</span><span class="n">__version__</span><span class="si">}</span><span class="s2">&quot;</span>

    <span class="k">def</span> <span class="nf">markdown</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;&lt;sup&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> [</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2">](</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">) </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2">&lt;/sup&gt;&quot;</span>

    <span class="k">def</span> <span class="nf">html</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;&lt;p&gt;&lt;sup&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s1"> &lt;a href=&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s1">&quot;&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s1">&lt;/a&gt; </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s1">&lt;/sup&gt;&lt;/p&gt;&#39;</span>

    <span class="k">def</span> <span class="nf">code_comment</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;# </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2"> &lt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">&gt;&quot;</span>

    <span class="k">def</span> <span class="nf">text</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2"> &lt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">&gt;&quot;</span>


<span class="k">class</span> <span class="nc">Reprex</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Abstract base class for a reprex instance. Concrete subclasses should implement the</span>
<span class="sd">    formatting logic appropriate to a specific venue for sharing.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">code_block</span><span class="p">:</span> <span class="n">CodeBlock</span><span class="p">,</span> <span class="n">advertise</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">:</span> <span class="n">CodeBlock</span> <span class="o">=</span> <span class="n">code_block</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_advertise</span> <span class="k">if</span> <span class="n">advertise</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">advertise</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">session_info</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
        <span class="k">pass</span>


<span class="k">class</span> <span class="nc">GitHubReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes in GitHub Flavored Markdown.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```python&quot;</span><span class="p">)</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">))</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">markdown</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&lt;details&gt;&lt;summary&gt;Session Info&lt;/summary&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```text&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">()))</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&lt;/details&gt;&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>


<span class="k">class</span> <span class="nc">HtmlReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is</span>
<span class="sd">    available, the rendered HTML will have syntax highlighting for the Python code.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">pygments</span> <span class="kn">import</span> <span class="n">highlight</span>
            <span class="kn">from</span> <span class="nn">pygments.lexers</span> <span class="kn">import</span> <span class="n">PythonLexer</span>
            <span class="kn">from</span> <span class="nn">pygments.formatters</span> <span class="kn">import</span> <span class="n">HtmlFormatter</span>

            <span class="n">formatter</span> <span class="o">=</span> <span class="n">HtmlFormatter</span><span class="p">()</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;&lt;style&gt;</span><span class="si">{</span><span class="n">formatter</span><span class="o">.</span><span class="n">get_style_defs</span><span class="p">(</span><span class="s1">&#39;.highlight&#39;</span><span class="p">)</span><span class="si">}</span><span class="s2">&lt;/style&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">highlight</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">),</span> <span class="n">PythonLexer</span><span class="p">(),</span> <span class="n">formatter</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;&lt;pre&gt;&lt;code&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="si">}</span><span class="s2">&lt;/code&gt;&lt;/pre&gt;&quot;</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">html</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&lt;details&gt;&lt;summary&gt;Session Info&lt;/summary&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;&lt;pre&gt;&lt;code&gt;</span><span class="si">{</span><span class="n">SessionInfo</span><span class="p">()</span><span class="si">}</span><span class="s2">&lt;/code&gt;&lt;/pre&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&lt;/details&gt;&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>


<span class="k">class</span> <span class="nc">PyScriptReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes as a Python script.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">)]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">code_comment</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
            <span class="n">sess_lines</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">())</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="s2">&quot;# &quot;</span> <span class="o">+</span> <span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">sess_lines</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>


<span class="k">class</span> <span class="nc">RtfReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes in Rich Text Format.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">pygments</span> <span class="kn">import</span> <span class="n">highlight</span>
            <span class="kn">from</span> <span class="nn">pygments.lexers</span> <span class="kn">import</span> <span class="n">PythonLexer</span>
            <span class="kn">from</span> <span class="nn">pygments.formatters</span> <span class="kn">import</span> <span class="n">RtfFormatter</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">&quot;Pygments is required for RTF output.&quot;</span><span class="p">)</span>

        <span class="n">out</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span> <span class="o">+=</span> <span class="s2">&quot;</span><span class="se">\n\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">text</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span> <span class="o">+=</span> <span class="s2">&quot;</span><span class="se">\n\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">highlight</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">PythonLexer</span><span class="p">(),</span> <span class="n">RtfFormatter</span><span class="p">())</span>


<span class="k">class</span> <span class="nc">SlackReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes as Slack markup.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">))</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">text</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">```&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">()))</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>


<span class="n">venues_dispatcher</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;gh&quot;</span><span class="p">:</span> <span class="n">GitHubReprex</span><span class="p">,</span>
    <span class="s2">&quot;so&quot;</span><span class="p">:</span> <span class="n">GitHubReprex</span><span class="p">,</span>
    <span class="s2">&quot;ds&quot;</span><span class="p">:</span> <span class="n">GitHubReprex</span><span class="p">,</span>
    <span class="s2">&quot;html&quot;</span><span class="p">:</span> <span class="n">HtmlReprex</span><span class="p">,</span>
    <span class="s2">&quot;py&quot;</span><span class="p">:</span> <span class="n">PyScriptReprex</span><span class="p">,</span>
    <span class="s2">&quot;rtf&quot;</span><span class="p">:</span> <span class="n">RtfReprex</span><span class="p">,</span>
    <span class="s2">&quot;slack&quot;</span><span class="p">:</span> <span class="n">SlackReprex</span><span class="p">,</span>
<span class="p">}</span>
<span class="sd">&quot;&quot;&quot;Mapping from venue keywords to their Reprex implementation.&quot;&quot;&quot;</span>


<span class="n">Venue</span> <span class="o">=</span> <span class="n">Enum</span><span class="p">(</span><span class="s2">&quot;Venue&quot;</span><span class="p">,</span> <span class="n">names</span><span class="o">=</span><span class="p">{</span><span class="n">v</span><span class="o">.</span><span class="n">upper</span><span class="p">():</span> <span class="n">v</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">venues_dispatcher</span><span class="o">.</span><span class="n">keys</span><span class="p">()},</span> <span class="nb">type</span><span class="o">=</span><span class="nb">str</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
<span class="n">Venue</span><span class="o">.</span><span class="vm">__doc__</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Enum for valid venue options.&quot;&quot;&quot;</span>


<span class="k">def</span> <span class="nf">reprex</span><span class="p">(</span>
    <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">outfile</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">venue</span><span class="o">=</span><span class="s2">&quot;gh&quot;</span><span class="p">,</span>
    <span class="n">advertise</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">,</span>
    <span class="n">print_</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">terminal</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Reprex</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Render reproducible examples of Python code for sharing. This function will evaluate your</span>
<span class="sd">    code and returns an instance of a [`Reprex`](reprexlite.reprex.Reprex) subclass. Calling</span>
<span class="sd">    `str(...)` on the `Reprex` object will return your code with the evaluated results embedded</span>
<span class="sd">    as comments, plus additional markup appropriate to the sharing venue set by the `venue` keyword</span>
<span class="sd">    argument.</span>

<span class="sd">    For example, for the `gh` venue for GitHub Flavored Markdown, you&#39;ll get a reprex whose string</span>
<span class="sd">    representation looks like:</span>

<span class="sd">    ````</span>
<span class="sd">    ```python</span>
<span class="sd">    x = 2</span>
<span class="sd">    x + 2</span>
<span class="sd">    #&gt; 4</span>
<span class="sd">    ```</span>

<span class="sd">    &lt;sup&gt;Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.1.0&lt;/sup&gt;</span>
<span class="sd">    ````</span>

<span class="sd">    The supported `venue` formats are:</span>

<span class="sd">    - `gh` : GitHub Flavored Markdown</span>
<span class="sd">    - `so` : StackOverflow, alias for gh</span>
<span class="sd">    - `ds` : Discourse, alias for gh</span>
<span class="sd">    - `html` : HTML</span>
<span class="sd">    - `py` : Python script</span>
<span class="sd">    - `rtf` : Rich Text Format</span>
<span class="sd">    - `slack` : Slack</span>

<span class="sd">    Args:</span>
<span class="sd">        input (str): Block of Python code</span>
<span class="sd">        outfile (Optional[Path]): Optional file path to write reprex to. Defaults to None.</span>
<span class="sd">        venue (str): Determines the output format by the venue you want to share the code. Defaults</span>
<span class="sd">            to &quot;gh&quot; for GitHub Flavored Markdown.</span>
<span class="sd">        advertise (Optional[bool]): Whether to include a note that links back to the reprexlite</span>
<span class="sd">            package. Default `None` will use the default set by choice of `venue`.</span>
<span class="sd">        session_info (bool): Whether to include additional details about your Python version,</span>
<span class="sd">            operating system, and installed packages. Defaults to False.</span>
<span class="sd">        style (bool): Whether to autoformat your code with black. Defaults to False.</span>
<span class="sd">        comment (str): Line prefix to use for displaying evaluated results. Defaults to &quot;#&gt;&quot;.</span>
<span class="sd">        print_ (bool): Whether to print your reprex to console. Defaults to True.</span>
<span class="sd">        terminal (bool): Whether to use syntax highlighting for 256-color terminal display.</span>
<span class="sd">            Requires optional dependency Pygments. Defaults to False.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Instance of a `Reprex` concrete subclass for `venue`.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">if</span> <span class="n">outfile</span> <span class="ow">or</span> <span class="n">venue</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">&quot;html&quot;</span><span class="p">,</span> <span class="s2">&quot;rtf&quot;</span><span class="p">]:</span>
        <span class="c1"># Don&#39;t screw output file or lexing for HTML and RTF with terminal syntax highlighting</span>
        <span class="n">terminal</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">code_block</span> <span class="o">=</span> <span class="n">CodeBlock</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">style</span><span class="p">,</span> <span class="n">comment</span><span class="o">=</span><span class="n">comment</span><span class="p">,</span> <span class="n">terminal</span><span class="o">=</span><span class="n">terminal</span><span class="p">)</span>

    <span class="n">reprex</span> <span class="o">=</span> <span class="n">venues_dispatcher</span><span class="p">[</span><span class="n">venue</span><span class="p">](</span>
        <span class="n">code_block</span><span class="o">=</span><span class="n">code_block</span><span class="p">,</span> <span class="n">advertise</span><span class="o">=</span><span class="n">advertise</span><span class="p">,</span> <span class="n">session_info</span><span class="o">=</span><span class="n">session_info</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">outfile</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">outfile</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">reprex</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">print_</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">reprex</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">reprex</span>
</pre></div>

        </details>

            </section>
                <section id="Advertisement">
                                <div class="attr class">
        <a class="headerlink" href="#Advertisement">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">Advertisement</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Advertisement</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class for generating the advertisement note for reprexlite.&quot;&quot;&quot;</span>

    <span class="n">pkg</span> <span class="o">=</span> <span class="s2">&quot;reprexlite&quot;</span>
    <span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;https://github.com/jayqi/reprexlite&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">now</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">astimezone</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S %Z&quot;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">created</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;Created at </span><span class="si">{</span><span class="n">now</span><span class="si">}</span><span class="s2"> by&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ver</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;v</span><span class="si">{</span><span class="n">__version__</span><span class="si">}</span><span class="s2">&quot;</span>

    <span class="k">def</span> <span class="nf">markdown</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;&lt;sup&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> [</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2">](</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">) </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2">&lt;/sup&gt;&quot;</span>

    <span class="k">def</span> <span class="nf">html</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;&lt;p&gt;&lt;sup&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s1"> &lt;a href=&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s1">&quot;&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s1">&lt;/a&gt; </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s1">&lt;/sup&gt;&lt;/p&gt;&#39;</span>

    <span class="k">def</span> <span class="nf">code_comment</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;# </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2"> &lt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">&gt;&quot;</span>

    <span class="k">def</span> <span class="nf">text</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2"> &lt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">&gt;&quot;</span>
</pre></div>

        </details>

            <div class="docstring"><p>Class for generating the advertisement note for reprexlite.</p>
</div>


                            <div id="Advertisement.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Advertisement.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">Advertisement</span><span class="signature">()</span>    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">now</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">astimezone</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S %Z&quot;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">created</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;Created at </span><span class="si">{</span><span class="n">now</span><span class="si">}</span><span class="s2"> by&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ver</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;v</span><span class="si">{</span><span class="n">__version__</span><span class="si">}</span><span class="s2">&quot;</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="Advertisement.pkg" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Advertisement.pkg">#&nbsp;&nbsp</a>

        <span class="name">pkg</span><span class="default_value"> = &#39;reprexlite&#39;</span>
    </div>

    

                            </div>
                            <div id="Advertisement.url" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Advertisement.url">#&nbsp;&nbsp</a>

        <span class="name">url</span><span class="default_value"> = &#39;https://github.com/jayqi/reprexlite&#39;</span>
    </div>

    

                            </div>
                            <div id="Advertisement.markdown" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Advertisement.markdown">#&nbsp;&nbsp</a>

        
            <span class="def">def</span>
            <span class="name">markdown</span><span class="signature">(self) -&gt; str</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="nf">markdown</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;&lt;sup&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> [</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2">](</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">) </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2">&lt;/sup&gt;&quot;</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="Advertisement.html" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Advertisement.html">#&nbsp;&nbsp</a>

        
            <span class="def">def</span>
            <span class="name">html</span><span class="signature">(self) -&gt; str</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="nf">html</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;&lt;p&gt;&lt;sup&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s1"> &lt;a href=&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s1">&quot;&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s1">&lt;/a&gt; </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s1">&lt;/sup&gt;&lt;/p&gt;&#39;</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="Advertisement.code_comment" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Advertisement.code_comment">#&nbsp;&nbsp</a>

        
            <span class="def">def</span>
            <span class="name">code_comment</span><span class="signature">(self) -&gt; str</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="nf">code_comment</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;# </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2"> &lt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">&gt;&quot;</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="Advertisement.text" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Advertisement.text">#&nbsp;&nbsp</a>

        
            <span class="def">def</span>
            <span class="name">text</span><span class="signature">(self) -&gt; str</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="nf">text</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">created</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">pkg</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">ver</span><span class="si">}</span><span class="s2"> &lt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="si">}</span><span class="s2">&gt;&quot;</span>
</pre></div>

        </details>

    

                            </div>
                </section>
                <section id="Reprex">
                                <div class="attr class">
        <a class="headerlink" href="#Reprex">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">Reprex</span>(<span class="base">abc.ABC</span>):
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Reprex</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Abstract base class for a reprex instance. Concrete subclasses should implement the</span>
<span class="sd">    formatting logic appropriate to a specific venue for sharing.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">code_block</span><span class="p">:</span> <span class="n">CodeBlock</span><span class="p">,</span> <span class="n">advertise</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">:</span> <span class="n">CodeBlock</span> <span class="o">=</span> <span class="n">code_block</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_advertise</span> <span class="k">if</span> <span class="n">advertise</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">advertise</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">session_info</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
        <span class="k">pass</span>
</pre></div>

        </details>

            <div class="docstring"><p>Abstract base class for a reprex instance. Concrete subclasses should implement the
formatting logic appropriate to a specific venue for sharing.</p>
</div>


                            <div id="Reprex.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Reprex.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">Reprex</span><span class="signature">(
    self,
    code_block: <a href="code.html#CodeBlock">reprexlite.code.CodeBlock</a>,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False
)</span>    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">code_block</span><span class="p">:</span> <span class="n">CodeBlock</span><span class="p">,</span> <span class="n">advertise</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">:</span> <span class="n">CodeBlock</span> <span class="o">=</span> <span class="n">code_block</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_advertise</span> <span class="k">if</span> <span class="n">advertise</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">advertise</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">session_info</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="Reprex.default_advertise" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Reprex.default_advertise">#&nbsp;&nbsp</a>

        <span class="name">default_advertise</span><span class="annotation">: bool</span>
    </div>

    

                            </div>
                            <div id="Reprex.code_block" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Reprex.code_block">#&nbsp;&nbsp</a>

        <span class="name">code_block</span><span class="annotation">: <a href="code.html#CodeBlock">reprexlite.code.CodeBlock</a></span>
    </div>

    

                            </div>
                            <div id="Reprex.advertise" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Reprex.advertise">#&nbsp;&nbsp</a>

        <span class="name">advertise</span><span class="annotation">: bool</span>
    </div>

    

                            </div>
                            <div id="Reprex.session_info" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Reprex.session_info">#&nbsp;&nbsp</a>

        <span class="name">session_info</span><span class="annotation">: bool</span>
    </div>

    

                            </div>
                </section>
                <section id="GitHubReprex">
                                <div class="attr class">
        <a class="headerlink" href="#GitHubReprex">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">GitHubReprex</span>(<span class="base"><a href="#Reprex">Reprex</a></span>):
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">GitHubReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes in GitHub Flavored Markdown.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```python&quot;</span><span class="p">)</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">))</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">markdown</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&lt;details&gt;&lt;summary&gt;Session Info&lt;/summary&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```text&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">()))</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&lt;/details&gt;&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>
</pre></div>

        </details>

            <div class="docstring"><p>Concrete implementation for rendering reprexes in GitHub Flavored Markdown.</p>
</div>


                            <div id="GitHubReprex.default_advertise" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#GitHubReprex.default_advertise">#&nbsp;&nbsp</a>

        <span class="name">default_advertise</span><span class="annotation">: bool</span><span class="default_value"> = True</span>
    </div>

    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#Reprex">reprexlite.reprex.Reprex</a></dt>
                                <dd id="GitHubReprex.__init__" class="function"><a href="#Reprex.__init__">Reprex</a></dd>
                <dd id="GitHubReprex.code_block" class="variable"><a href="#Reprex.code_block">code_block</a></dd>
                <dd id="GitHubReprex.advertise" class="variable"><a href="#Reprex.advertise">advertise</a></dd>
                <dd id="GitHubReprex.session_info" class="variable"><a href="#Reprex.session_info">session_info</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="HtmlReprex">
                                <div class="attr class">
        <a class="headerlink" href="#HtmlReprex">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">HtmlReprex</span>(<span class="base"><a href="#Reprex">Reprex</a></span>):
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">HtmlReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is</span>
<span class="sd">    available, the rendered HTML will have syntax highlighting for the Python code.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">pygments</span> <span class="kn">import</span> <span class="n">highlight</span>
            <span class="kn">from</span> <span class="nn">pygments.lexers</span> <span class="kn">import</span> <span class="n">PythonLexer</span>
            <span class="kn">from</span> <span class="nn">pygments.formatters</span> <span class="kn">import</span> <span class="n">HtmlFormatter</span>

            <span class="n">formatter</span> <span class="o">=</span> <span class="n">HtmlFormatter</span><span class="p">()</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;&lt;style&gt;</span><span class="si">{</span><span class="n">formatter</span><span class="o">.</span><span class="n">get_style_defs</span><span class="p">(</span><span class="s1">&#39;.highlight&#39;</span><span class="p">)</span><span class="si">}</span><span class="s2">&lt;/style&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">highlight</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">),</span> <span class="n">PythonLexer</span><span class="p">(),</span> <span class="n">formatter</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;&lt;pre&gt;&lt;code&gt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="si">}</span><span class="s2">&lt;/code&gt;&lt;/pre&gt;&quot;</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">html</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&lt;details&gt;&lt;summary&gt;Session Info&lt;/summary&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;&lt;pre&gt;&lt;code&gt;</span><span class="si">{</span><span class="n">SessionInfo</span><span class="p">()</span><span class="si">}</span><span class="s2">&lt;/code&gt;&lt;/pre&gt;&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&lt;/details&gt;&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>
</pre></div>

        </details>

            <div class="docstring"><p>Concrete implementation for rendering reprexes in HTML. If optional dependency Pygments is
available, the rendered HTML will have syntax highlighting for the Python code.</p>
</div>


                            <div id="HtmlReprex.default_advertise" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#HtmlReprex.default_advertise">#&nbsp;&nbsp</a>

        <span class="name">default_advertise</span><span class="annotation">: bool</span><span class="default_value"> = True</span>
    </div>

    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#Reprex">reprexlite.reprex.Reprex</a></dt>
                                <dd id="HtmlReprex.__init__" class="function"><a href="#Reprex.__init__">Reprex</a></dd>
                <dd id="HtmlReprex.code_block" class="variable"><a href="#Reprex.code_block">code_block</a></dd>
                <dd id="HtmlReprex.advertise" class="variable"><a href="#Reprex.advertise">advertise</a></dd>
                <dd id="HtmlReprex.session_info" class="variable"><a href="#Reprex.session_info">session_info</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="PyScriptReprex">
                                <div class="attr class">
        <a class="headerlink" href="#PyScriptReprex">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">PyScriptReprex</span>(<span class="base"><a href="#Reprex">Reprex</a></span>):
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">PyScriptReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes as a Python script.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">)]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">code_comment</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
            <span class="n">sess_lines</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">())</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="s2">&quot;# &quot;</span> <span class="o">+</span> <span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">sess_lines</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>
</pre></div>

        </details>

            <div class="docstring"><p>Concrete implementation for rendering reprexes as a Python script.</p>
</div>


                            <div id="PyScriptReprex.default_advertise" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#PyScriptReprex.default_advertise">#&nbsp;&nbsp</a>

        <span class="name">default_advertise</span><span class="annotation">: bool</span><span class="default_value"> = False</span>
    </div>

    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#Reprex">reprexlite.reprex.Reprex</a></dt>
                                <dd id="PyScriptReprex.__init__" class="function"><a href="#Reprex.__init__">Reprex</a></dd>
                <dd id="PyScriptReprex.code_block" class="variable"><a href="#Reprex.code_block">code_block</a></dd>
                <dd id="PyScriptReprex.advertise" class="variable"><a href="#Reprex.advertise">advertise</a></dd>
                <dd id="PyScriptReprex.session_info" class="variable"><a href="#Reprex.session_info">session_info</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="RtfReprex">
                                <div class="attr class">
        <a class="headerlink" href="#RtfReprex">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">RtfReprex</span>(<span class="base"><a href="#Reprex">Reprex</a></span>):
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">RtfReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes in Rich Text Format.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">pygments</span> <span class="kn">import</span> <span class="n">highlight</span>
            <span class="kn">from</span> <span class="nn">pygments.lexers</span> <span class="kn">import</span> <span class="n">PythonLexer</span>
            <span class="kn">from</span> <span class="nn">pygments.formatters</span> <span class="kn">import</span> <span class="n">RtfFormatter</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">&quot;Pygments is required for RTF output.&quot;</span><span class="p">)</span>

        <span class="n">out</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span> <span class="o">+=</span> <span class="s2">&quot;</span><span class="se">\n\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">text</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span> <span class="o">+=</span> <span class="s2">&quot;</span><span class="se">\n\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">())</span>
        <span class="k">return</span> <span class="n">highlight</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">PythonLexer</span><span class="p">(),</span> <span class="n">RtfFormatter</span><span class="p">())</span>
</pre></div>

        </details>

            <div class="docstring"><p>Concrete implementation for rendering reprexes in Rich Text Format.</p>
</div>


                            <div id="RtfReprex.default_advertise" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#RtfReprex.default_advertise">#&nbsp;&nbsp</a>

        <span class="name">default_advertise</span><span class="annotation">: bool</span><span class="default_value"> = False</span>
    </div>

    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#Reprex">reprexlite.reprex.Reprex</a></dt>
                                <dd id="RtfReprex.__init__" class="function"><a href="#Reprex.__init__">Reprex</a></dd>
                <dd id="RtfReprex.code_block" class="variable"><a href="#Reprex.code_block">code_block</a></dd>
                <dd id="RtfReprex.advertise" class="variable"><a href="#Reprex.advertise">advertise</a></dd>
                <dd id="RtfReprex.session_info" class="variable"><a href="#Reprex.session_info">session_info</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SlackReprex">
                                <div class="attr class">
        <a class="headerlink" href="#SlackReprex">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">SlackReprex</span>(<span class="base"><a href="#Reprex">Reprex</a></span>):
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">SlackReprex</span><span class="p">(</span><span class="n">Reprex</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Concrete implementation for rendering reprexes as Slack markup.&quot;&quot;&quot;</span>

    <span class="n">default_advertise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_block</span><span class="p">))</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">advertise</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="o">+</span> <span class="n">Advertisement</span><span class="p">()</span><span class="o">.</span><span class="n">text</span><span class="p">())</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">session_info</span><span class="p">:</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">```&quot;</span><span class="p">)</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">SessionInfo</span><span class="p">()))</span>
            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">&quot;```&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>
</pre></div>

        </details>

            <div class="docstring"><p>Concrete implementation for rendering reprexes as Slack markup.</p>
</div>


                            <div id="SlackReprex.default_advertise" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#SlackReprex.default_advertise">#&nbsp;&nbsp</a>

        <span class="name">default_advertise</span><span class="annotation">: bool</span><span class="default_value"> = False</span>
    </div>

    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#Reprex">reprexlite.reprex.Reprex</a></dt>
                                <dd id="SlackReprex.__init__" class="function"><a href="#Reprex.__init__">Reprex</a></dd>
                <dd id="SlackReprex.code_block" class="variable"><a href="#Reprex.code_block">code_block</a></dd>
                <dd id="SlackReprex.advertise" class="variable"><a href="#Reprex.advertise">advertise</a></dd>
                <dd id="SlackReprex.session_info" class="variable"><a href="#Reprex.session_info">session_info</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="venues_dispatcher">
                                <div class="attr variable"><a class="headerlink" href="#venues_dispatcher">#&nbsp;&nbsp</a>

        <span class="name">venues_dispatcher</span><span class="annotation">: Dict[str, Callable]</span><span class="default_value"> = {&#39;gh&#39;: &lt;class &#39;<a href="#GitHubReprex">reprexlite.reprex.GitHubReprex</a>&#39;&gt;, &#39;so&#39;: &lt;class &#39;<a href="#GitHubReprex">reprexlite.reprex.GitHubReprex</a>&#39;&gt;, &#39;ds&#39;: &lt;class &#39;<a href="#GitHubReprex">reprexlite.reprex.GitHubReprex</a>&#39;&gt;, &#39;html&#39;: &lt;class &#39;<a href="#HtmlReprex">reprexlite.reprex.HtmlReprex</a>&#39;&gt;, &#39;py&#39;: &lt;class &#39;<a href="#PyScriptReprex">reprexlite.reprex.PyScriptReprex</a>&#39;&gt;, &#39;rtf&#39;: &lt;class &#39;<a href="#RtfReprex">reprexlite.reprex.RtfReprex</a>&#39;&gt;, &#39;slack&#39;: &lt;class &#39;<a href="#SlackReprex">reprexlite.reprex.SlackReprex</a>&#39;&gt;}</span>
    </div>

            <div class="docstring"><p>Mapping from venue keywords to their Reprex implementation.</p>
</div>


                </section>
                <section id="Venue">
                                <div class="attr class">
        <a class="headerlink" href="#Venue">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">Venue</span>(<span class="base">builtins.str</span>, <span class="base">enum.Enum</span>):
    </div>

        
            <div class="docstring"><p>Enum for valid venue options.</p>
</div>


                            <div id="Venue.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Venue.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">Venue</span><span class="signature">()</span>    </div>

        
    

                            </div>
                            <div id="Venue.GH" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Venue.GH">#&nbsp;&nbsp</a>

        <span class="name">GH</span><span class="default_value"> = &lt;<a href="#Venue.GH">Venue.GH</a>: &#39;gh&#39;&gt;</span>
    </div>

    

                            </div>
                            <div id="Venue.SO" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Venue.SO">#&nbsp;&nbsp</a>

        <span class="name">SO</span><span class="default_value"> = &lt;<a href="#Venue.SO">Venue.SO</a>: &#39;so&#39;&gt;</span>
    </div>

    

                            </div>
                            <div id="Venue.DS" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Venue.DS">#&nbsp;&nbsp</a>

        <span class="name">DS</span><span class="default_value"> = &lt;<a href="#Venue.DS">Venue.DS</a>: &#39;ds&#39;&gt;</span>
    </div>

    

                            </div>
                            <div id="Venue.HTML" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Venue.HTML">#&nbsp;&nbsp</a>

        <span class="name">HTML</span><span class="default_value"> = &lt;<a href="#Venue.HTML">Venue.HTML</a>: &#39;html&#39;&gt;</span>
    </div>

    

                            </div>
                            <div id="Venue.PY" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Venue.PY">#&nbsp;&nbsp</a>

        <span class="name">PY</span><span class="default_value"> = &lt;<a href="#Venue.PY">Venue.PY</a>: &#39;py&#39;&gt;</span>
    </div>

    

                            </div>
                            <div id="Venue.RTF" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Venue.RTF">#&nbsp;&nbsp</a>

        <span class="name">RTF</span><span class="default_value"> = &lt;<a href="#Venue.RTF">Venue.RTF</a>: &#39;rtf&#39;&gt;</span>
    </div>

    

                            </div>
                            <div id="Venue.SLACK" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Venue.SLACK">#&nbsp;&nbsp</a>

        <span class="name">SLACK</span><span class="default_value"> = &lt;<a href="#Venue.SLACK">Venue.SLACK</a>: &#39;slack&#39;&gt;</span>
    </div>

    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="Venue.name" class="variable">name</dd>
                <dd id="Venue.value" class="variable">value</dd>

            </div>
            <div><dt>builtins.str</dt>
                                <dd id="Venue.encode" class="function">encode</dd>
                <dd id="Venue.replace" class="function">replace</dd>
                <dd id="Venue.split" class="function">split</dd>
                <dd id="Venue.rsplit" class="function">rsplit</dd>
                <dd id="Venue.join" class="function">join</dd>
                <dd id="Venue.capitalize" class="function">capitalize</dd>
                <dd id="Venue.casefold" class="function">casefold</dd>
                <dd id="Venue.title" class="function">title</dd>
                <dd id="Venue.center" class="function">center</dd>
                <dd id="Venue.count" class="function">count</dd>
                <dd id="Venue.expandtabs" class="function">expandtabs</dd>
                <dd id="Venue.find" class="function">find</dd>
                <dd id="Venue.partition" class="function">partition</dd>
                <dd id="Venue.index" class="function">index</dd>
                <dd id="Venue.ljust" class="function">ljust</dd>
                <dd id="Venue.lower" class="function">lower</dd>
                <dd id="Venue.lstrip" class="function">lstrip</dd>
                <dd id="Venue.rfind" class="function">rfind</dd>
                <dd id="Venue.rindex" class="function">rindex</dd>
                <dd id="Venue.rjust" class="function">rjust</dd>
                <dd id="Venue.rstrip" class="function">rstrip</dd>
                <dd id="Venue.rpartition" class="function">rpartition</dd>
                <dd id="Venue.splitlines" class="function">splitlines</dd>
                <dd id="Venue.strip" class="function">strip</dd>
                <dd id="Venue.swapcase" class="function">swapcase</dd>
                <dd id="Venue.translate" class="function">translate</dd>
                <dd id="Venue.upper" class="function">upper</dd>
                <dd id="Venue.startswith" class="function">startswith</dd>
                <dd id="Venue.endswith" class="function">endswith</dd>
                <dd id="Venue.isascii" class="function">isascii</dd>
                <dd id="Venue.islower" class="function">islower</dd>
                <dd id="Venue.isupper" class="function">isupper</dd>
                <dd id="Venue.istitle" class="function">istitle</dd>
                <dd id="Venue.isspace" class="function">isspace</dd>
                <dd id="Venue.isdecimal" class="function">isdecimal</dd>
                <dd id="Venue.isdigit" class="function">isdigit</dd>
                <dd id="Venue.isnumeric" class="function">isnumeric</dd>
                <dd id="Venue.isalpha" class="function">isalpha</dd>
                <dd id="Venue.isalnum" class="function">isalnum</dd>
                <dd id="Venue.isidentifier" class="function">isidentifier</dd>
                <dd id="Venue.isprintable" class="function">isprintable</dd>
                <dd id="Venue.zfill" class="function">zfill</dd>
                <dd id="Venue.format" class="function">format</dd>
                <dd id="Venue.format_map" class="function">format_map</dd>
                <dd id="Venue.maketrans" class="function">maketrans</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="reprex">
                            <div class="attr function"><a class="headerlink" href="#reprex">#&nbsp;&nbsp</a>

        
            <span class="def">def</span>
            <span class="name">reprex</span><span class="signature">(
    input: str,
    outfile: Union[pathlib.Path, NoneType] = None,
    venue=&#39;gh&#39;,
    advertise: Union[bool, NoneType] = None,
    session_info: bool = False,
    style: bool = False,
    comment: str = &#39;#&gt;&#39;,
    print_=True,
    terminal=False
) -&gt; <a href="#Reprex">reprexlite.reprex.Reprex</a></span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">def</span> <span class="nf">reprex</span><span class="p">(</span>
    <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">outfile</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">venue</span><span class="o">=</span><span class="s2">&quot;gh&quot;</span><span class="p">,</span>
    <span class="n">advertise</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">session_info</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">,</span>
    <span class="n">print_</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">terminal</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Reprex</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Render reproducible examples of Python code for sharing. This function will evaluate your</span>
<span class="sd">    code and returns an instance of a [`Reprex`](reprexlite.reprex.Reprex) subclass. Calling</span>
<span class="sd">    `str(...)` on the `Reprex` object will return your code with the evaluated results embedded</span>
<span class="sd">    as comments, plus additional markup appropriate to the sharing venue set by the `venue` keyword</span>
<span class="sd">    argument.</span>

<span class="sd">    For example, for the `gh` venue for GitHub Flavored Markdown, you&#39;ll get a reprex whose string</span>
<span class="sd">    representation looks like:</span>

<span class="sd">    ````</span>
<span class="sd">    ```python</span>
<span class="sd">    x = 2</span>
<span class="sd">    x + 2</span>
<span class="sd">    #&gt; 4</span>
<span class="sd">    ```</span>

<span class="sd">    &lt;sup&gt;Created at 2021-02-15 16:58:47 PST by [reprexlite](https://github.com/jayqi/reprexlite) v0.1.0&lt;/sup&gt;</span>
<span class="sd">    ````</span>

<span class="sd">    The supported `venue` formats are:</span>

<span class="sd">    - `gh` : GitHub Flavored Markdown</span>
<span class="sd">    - `so` : StackOverflow, alias for gh</span>
<span class="sd">    - `ds` : Discourse, alias for gh</span>
<span class="sd">    - `html` : HTML</span>
<span class="sd">    - `py` : Python script</span>
<span class="sd">    - `rtf` : Rich Text Format</span>
<span class="sd">    - `slack` : Slack</span>

<span class="sd">    Args:</span>
<span class="sd">        input (str): Block of Python code</span>
<span class="sd">        outfile (Optional[Path]): Optional file path to write reprex to. Defaults to None.</span>
<span class="sd">        venue (str): Determines the output format by the venue you want to share the code. Defaults</span>
<span class="sd">            to &quot;gh&quot; for GitHub Flavored Markdown.</span>
<span class="sd">        advertise (Optional[bool]): Whether to include a note that links back to the reprexlite</span>
<span class="sd">            package. Default `None` will use the default set by choice of `venue`.</span>
<span class="sd">        session_info (bool): Whether to include additional details about your Python version,</span>
<span class="sd">            operating system, and installed packages. Defaults to False.</span>
<span class="sd">        style (bool): Whether to autoformat your code with black. Defaults to False.</span>
<span class="sd">        comment (str): Line prefix to use for displaying evaluated results. Defaults to &quot;#&gt;&quot;.</span>
<span class="sd">        print_ (bool): Whether to print your reprex to console. Defaults to True.</span>
<span class="sd">        terminal (bool): Whether to use syntax highlighting for 256-color terminal display.</span>
<span class="sd">            Requires optional dependency Pygments. Defaults to False.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Instance of a `Reprex` concrete subclass for `venue`.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">if</span> <span class="n">outfile</span> <span class="ow">or</span> <span class="n">venue</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">&quot;html&quot;</span><span class="p">,</span> <span class="s2">&quot;rtf&quot;</span><span class="p">]:</span>
        <span class="c1"># Don&#39;t screw output file or lexing for HTML and RTF with terminal syntax highlighting</span>
        <span class="n">terminal</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">code_block</span> <span class="o">=</span> <span class="n">CodeBlock</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">style</span><span class="p">,</span> <span class="n">comment</span><span class="o">=</span><span class="n">comment</span><span class="p">,</span> <span class="n">terminal</span><span class="o">=</span><span class="n">terminal</span><span class="p">)</span>

    <span class="n">reprex</span> <span class="o">=</span> <span class="n">venues_dispatcher</span><span class="p">[</span><span class="n">venue</span><span class="p">](</span>
        <span class="n">code_block</span><span class="o">=</span><span class="n">code_block</span><span class="p">,</span> <span class="n">advertise</span><span class="o">=</span><span class="n">advertise</span><span class="p">,</span> <span class="n">session_info</span><span class="o">=</span><span class="n">session_info</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">outfile</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">outfile</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">reprex</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">print_</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">reprex</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">reprex</span>
</pre></div>

        </details>

            <div class="docstring"><p>Render reproducible examples of Python code for sharing. This function will evaluate your
code and returns an instance of a <a href="<a href="#Reprex">reprexlite.reprex.Reprex</a>"><code><a href="#Reprex">Reprex</a></code></a> subclass. Calling
<code>str(...)</code> on the <code><a href="#Reprex">Reprex</a></code> object will return your code with the evaluated results embedded
as comments, plus additional markup appropriate to the sharing venue set by the <code>venue</code> keyword
argument.</p>

<p>For example, for the <code>gh</code> venue for GitHub Flavored Markdown, you'll get a reprex whose string
representation looks like:</p>

<p>````</p>

<div class="codehilite"><pre><span></span><code><span class="n">x</span> <span class="o">=</span> <span class="mi">2</span>
<span class="n">x</span> <span class="o">+</span> <span class="mi">2</span>
<span class="c1">#&gt; 4</span>
</code></pre></div>

<p><sup>Created at 2021-02-15 16:58:47 PST by <a href="https://github.com/jayqi/reprexlite">reprexlite</a> v0.1.0</sup>
````</p>

<p>The supported <code>venue</code> formats are:</p>

<ul>
<li><code>gh</code> : GitHub Flavored Markdown</li>
<li><code>so</code> : StackOverflow, alias for gh</li>
<li><code>ds</code> : Discourse, alias for gh</li>
<li><code>html</code> : HTML</li>
<li><code>py</code> : Python script</li>
<li><code>rtf</code> : Rich Text Format</li>
<li><code>slack</code> : Slack</li>
</ul>

<p>Args:
    input (str): Block of Python code
    outfile (Optional[Path]): Optional file path to write reprex to. Defaults to None.
    venue (str): Determines the output format by the venue you want to share the code. Defaults
        to "gh" for GitHub Flavored Markdown.
    advertise (Optional[bool]): Whether to include a note that links back to the reprexlite
        package. Default <code>None</code> will use the default set by choice of <code>venue</code>.
    session_info (bool): Whether to include additional details about your Python version,
        operating system, and installed packages. Defaults to False.
    style (bool): Whether to autoformat your code with black. Defaults to False.
    comment (str): Line prefix to use for displaying evaluated results. Defaults to "#&gt;".
    print_ (bool): Whether to print your reprex to console. Defaults to True.
    terminal (bool): Whether to use syntax highlighting for 256-color terminal display.
        Requires optional dependency Pygments. Defaults to False.</p>

<p>Returns:
    Instance of a <code><a href="#Reprex">Reprex</a></code> concrete subclass for <code>venue</code>.</p>
</div>


                </section>
    </main>
</div>