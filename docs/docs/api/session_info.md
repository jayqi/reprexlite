---
title: reprexlite.session_info
---
<div>

<style type="text/css">/*! pygments syntax highlighting */pre{line-height:125%;}td.linenos pre{color:#000000; background-color:#f0f0f0; padding-left:5px; padding-right:5px;}span.linenos{color:#000000; background-color:#f0f0f0; padding-left:5px; padding-right:5px;}td.linenos pre.special{color:#000000; background-color:#ffffc0; padding-left:5px; padding-right:5px;}span.linenos.special{color:#000000; background-color:#ffffc0; padding-left:5px; padding-right:5px;}.pdoc .hll{background-color:#ffffcc}.pdoc{background:#f8f8f8;}.pdoc .c{color:#408080; font-style:italic}.pdoc .err{border:1px solid #FF0000}.pdoc .k{color:#008000; font-weight:bold}.pdoc .o{color:#666666}.pdoc .ch{color:#408080; font-style:italic}.pdoc .cm{color:#408080; font-style:italic}.pdoc .cp{color:#BC7A00}.pdoc .cpf{color:#408080; font-style:italic}.pdoc .c1{color:#408080; font-style:italic}.pdoc .cs{color:#408080; font-style:italic}.pdoc .gd{color:#A00000}.pdoc .ge{font-style:italic}.pdoc .gr{color:#FF0000}.pdoc .gh{color:#000080; font-weight:bold}.pdoc .gi{color:#00A000}.pdoc .go{color:#888888}.pdoc .gp{color:#000080; font-weight:bold}.pdoc .gs{font-weight:bold}.pdoc .gu{color:#800080; font-weight:bold}.pdoc .gt{color:#0044DD}.pdoc .kc{color:#008000; font-weight:bold}.pdoc .kd{color:#008000; font-weight:bold}.pdoc .kn{color:#008000; font-weight:bold}.pdoc .kp{color:#008000}.pdoc .kr{color:#008000; font-weight:bold}.pdoc .kt{color:#B00040}.pdoc .m{color:#666666}.pdoc .s{color:#BA2121}.pdoc .na{color:#7D9029}.pdoc .nb{color:#008000}.pdoc .nc{color:#0000FF; font-weight:bold}.pdoc .no{color:#880000}.pdoc .nd{color:#AA22FF}.pdoc .ni{color:#999999; font-weight:bold}.pdoc .ne{color:#D2413A; font-weight:bold}.pdoc .nf{color:#0000FF}.pdoc .nl{color:#A0A000}.pdoc .nn{color:#0000FF; font-weight:bold}.pdoc .nt{color:#008000; font-weight:bold}.pdoc .nv{color:#19177C}.pdoc .ow{color:#AA22FF; font-weight:bold}.pdoc .w{color:#bbbbbb}.pdoc .mb{color:#666666}.pdoc .mf{color:#666666}.pdoc .mh{color:#666666}.pdoc .mi{color:#666666}.pdoc .mo{color:#666666}.pdoc .sa{color:#BA2121}.pdoc .sb{color:#BA2121}.pdoc .sc{color:#BA2121}.pdoc .dl{color:#BA2121}.pdoc .sd{color:#BA2121; font-style:italic}.pdoc .s2{color:#BA2121}.pdoc .se{color:#BB6622; font-weight:bold}.pdoc .sh{color:#BA2121}.pdoc .si{color:#BB6688; font-weight:bold}.pdoc .sx{color:#008000}.pdoc .sr{color:#BB6688}.pdoc .s1{color:#BA2121}.pdoc .ss{color:#19177C}.pdoc .bp{color:#008000}.pdoc .fm{color:#0000FF}.pdoc .vc{color:#19177C}.pdoc .vg{color:#19177C}.pdoc .vi{color:#19177C}.pdoc .vm{color:#19177C}.pdoc .il{color:#666666}</style>
<style type="text/css">/*! pdoc */:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f7f7f7;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}html, main{scroll-behavior:smooth;}.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3, .pdoc h4{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{background-color:var(--code);border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--code);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.pdoc details{--shift:-40px;text-align:right;margin-top:var(--shift);margin-bottom:calc(0px - var(--shift));clear:both;filter:opacity(1);}.pdoc details:not([open]){height:0;overflow:visible;}.pdoc details > summary{font-size:.75rem;cursor:pointer;color:var(--muted);border-width:0;padding:0 .7em;display:inline-block;display:inline list-item;user-select:none;}.pdoc details > summary:focus{outline:0;}.pdoc details > div{margin-top:calc(0px - var(--shift) / 2);text-align:left;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc > section:first-of-type > .docstring{margin-bottom:3rem;}.pdoc .docstring pre{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc .headerlink{position:absolute;width:0;margin-left:-1.5rem;line-height:1.4rem;font-size:1.5rem;font-weight:normal;transition:all 100ms ease-in-out;opacity:0;}.pdoc .attr > .headerlink{margin-left:-2.5rem;}.pdoc *:hover > .headerlink,.pdoc *:target > .attr > .headerlink{opacity:1;}.pdoc .attr{color:var(--text);margin:1rem 0 .5rem;padding:.4rem 5rem .4rem 1rem;background-color:var(--accent);}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{white-space:pre-wrap;}.pdoc .annotation{color:var(--annotation);}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}</style>    <main class="pdoc">
            <section>
                    <h1 class="modulename">
reprexlite.session_info    </h1>

                
                        <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="nn">platform</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">List</span><span class="p">,</span> <span class="n">Tuple</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">8</span><span class="p">):</span>
    <span class="kn">import</span> <span class="nn">importlib.metadata</span> <span class="k">as</span> <span class="nn">importlib_metadata</span>
<span class="k">else</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">importlib_metadata</span>


<span class="k">class</span> <span class="nc">SessionInfo</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class for pretty-formatting Python session info. Includes details about your Python version,</span>
<span class="sd">    your operating system, and the Python packages installed in your current environment.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">python_version</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_version</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">python_build_date</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_build</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">os</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">platform</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">packages</span> <span class="o">=</span> <span class="p">[</span><span class="n">Package</span><span class="p">(</span><span class="n">distr</span><span class="p">)</span> <span class="k">for</span> <span class="n">distr</span> <span class="ow">in</span> <span class="n">importlib_metadata</span><span class="o">.</span><span class="n">Distribution</span><span class="o">.</span><span class="n">discover</span><span class="p">()]</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;-- Session Info --&quot;</span> <span class="o">+</span> <span class="s2">&quot;-&quot;</span> <span class="o">*</span> <span class="mi">60</span><span class="p">]</span>
        <span class="n">lines</span> <span class="o">+=</span> <span class="n">tabulate</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="p">(</span><span class="s2">&quot;version&quot;</span><span class="p">,</span> <span class="sa">f</span><span class="s2">&quot;Python </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">python_version</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">python_build_date</span><span class="si">}</span><span class="s2">)&quot;</span><span class="p">),</span>
                <span class="p">(</span><span class="s2">&quot;os&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">os</span><span class="p">),</span>
            <span class="p">]</span>
        <span class="p">)</span>
        <span class="n">lines</span> <span class="o">+=</span> <span class="p">[</span><span class="s2">&quot;-- Packages --&quot;</span> <span class="o">+</span> <span class="s2">&quot;-&quot;</span> <span class="o">*</span> <span class="mi">64</span><span class="p">]</span>
        <span class="n">lines</span> <span class="o">+=</span> <span class="n">tabulate</span><span class="p">([(</span><span class="n">pkg</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">pkg</span><span class="o">.</span><span class="n">version</span><span class="p">)</span> <span class="k">for</span> <span class="n">pkg</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">packages</span><span class="p">)])</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>


<span class="k">class</span> <span class="nc">Package</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Interface for adapting [`importlib.metadata.Distribution`](https://docs.python.org/3/library/importlib.metadata.html#distributions)</span>
<span class="sd">    instances for introspection by [`SessionInfo`][reprexlite.session_info.SessionInfo].</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">distribution</span><span class="p">:</span> <span class="n">importlib_metadata</span><span class="o">.</span><span class="n">Distribution</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span> <span class="o">=</span> <span class="n">distribution</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">&quot;Name&quot;</span><span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">version</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">version</span>

    <span class="k">def</span> <span class="fm">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">Package</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">&lt;</span> <span class="n">other</span><span class="o">.</span><span class="n">name</span>


<span class="k">def</span> <span class="nf">tabulate</span><span class="p">(</span><span class="n">rows</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
    <span class="n">left_max</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">)</span>
    <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">left</span><span class="p">,</span> <span class="n">right</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">:</span>
        <span class="n">padding</span> <span class="o">=</span> <span class="p">(</span><span class="n">left_max</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="nb">len</span><span class="p">(</span><span class="n">left</span><span class="p">))</span> <span class="o">*</span> <span class="s2">&quot; &quot;</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">left</span> <span class="o">+</span> <span class="n">padding</span> <span class="o">+</span> <span class="n">right</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">out</span>
</pre></div>

        </details>

            </section>
                <section id="SessionInfo">
                                <div class="attr class">
        <a class="headerlink" href="#SessionInfo">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">SessionInfo</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">SessionInfo</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class for pretty-formatting Python session info. Includes details about your Python version,</span>
<span class="sd">    your operating system, and the Python packages installed in your current environment.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">python_version</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_version</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">python_build_date</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_build</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">os</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">platform</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">packages</span> <span class="o">=</span> <span class="p">[</span><span class="n">Package</span><span class="p">(</span><span class="n">distr</span><span class="p">)</span> <span class="k">for</span> <span class="n">distr</span> <span class="ow">in</span> <span class="n">importlib_metadata</span><span class="o">.</span><span class="n">Distribution</span><span class="o">.</span><span class="n">discover</span><span class="p">()]</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;-- Session Info --&quot;</span> <span class="o">+</span> <span class="s2">&quot;-&quot;</span> <span class="o">*</span> <span class="mi">60</span><span class="p">]</span>
        <span class="n">lines</span> <span class="o">+=</span> <span class="n">tabulate</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="p">(</span><span class="s2">&quot;version&quot;</span><span class="p">,</span> <span class="sa">f</span><span class="s2">&quot;Python </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">python_version</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">python_build_date</span><span class="si">}</span><span class="s2">)&quot;</span><span class="p">),</span>
                <span class="p">(</span><span class="s2">&quot;os&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">os</span><span class="p">),</span>
            <span class="p">]</span>
        <span class="p">)</span>
        <span class="n">lines</span> <span class="o">+=</span> <span class="p">[</span><span class="s2">&quot;-- Packages --&quot;</span> <span class="o">+</span> <span class="s2">&quot;-&quot;</span> <span class="o">*</span> <span class="mi">64</span><span class="p">]</span>
        <span class="n">lines</span> <span class="o">+=</span> <span class="n">tabulate</span><span class="p">([(</span><span class="n">pkg</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">pkg</span><span class="o">.</span><span class="n">version</span><span class="p">)</span> <span class="k">for</span> <span class="n">pkg</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">packages</span><span class="p">)])</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</pre></div>

        </details>

            <div class="docstring"><p>Class for pretty-formatting Python session info. Includes details about your Python version,
your operating system, and the Python packages installed in your current environment.</p>
</div>


                            <div id="SessionInfo.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#SessionInfo.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">SessionInfo</span><span class="signature">()</span>    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">python_version</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_version</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">python_build_date</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_build</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">os</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">platform</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">packages</span> <span class="o">=</span> <span class="p">[</span><span class="n">Package</span><span class="p">(</span><span class="n">distr</span><span class="p">)</span> <span class="k">for</span> <span class="n">distr</span> <span class="ow">in</span> <span class="n">importlib_metadata</span><span class="o">.</span><span class="n">Distribution</span><span class="o">.</span><span class="n">discover</span><span class="p">()]</span>
</pre></div>

        </details>

    

                            </div>
                </section>
                <section id="Package">
                                <div class="attr class">
        <a class="headerlink" href="#Package">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">Package</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Package</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Interface for adapting [`importlib.metadata.Distribution`](https://docs.python.org/3/library/importlib.metadata.html#distributions)</span>
<span class="sd">    instances for introspection by [`SessionInfo`][reprexlite.session_info.SessionInfo].</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">distribution</span><span class="p">:</span> <span class="n">importlib_metadata</span><span class="o">.</span><span class="n">Distribution</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span> <span class="o">=</span> <span class="n">distribution</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">&quot;Name&quot;</span><span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">version</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">version</span>

    <span class="k">def</span> <span class="fm">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">Package</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">&lt;</span> <span class="n">other</span><span class="o">.</span><span class="n">name</span>
</pre></div>

        </details>

            <div class="docstring"><p>Interface for adapting <a href="https://docs.python.org/3/library/importlib.metadata.html#distributions"><code>importlib.metadata.Distribution</code></a>
instances for introspection by [<code><a href="#SessionInfo">SessionInfo</a></code>][<a href="#SessionInfo">reprexlite.session_info.SessionInfo</a>].</p>
</div>


                            <div id="Package.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Package.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">Package</span><span class="signature">(distribution: importlib.metadata.Distribution)</span>    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">distribution</span><span class="p">:</span> <span class="n">importlib_metadata</span><span class="o">.</span><span class="n">Distribution</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span> <span class="o">=</span> <span class="n">distribution</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="Package.name" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Package.name">#&nbsp;&nbsp</a>

        <span class="name">name</span><span class="annotation">: str</span>
    </div>

    

                            </div>
                            <div id="Package.version" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#Package.version">#&nbsp;&nbsp</a>

        <span class="name">version</span><span class="annotation">: str</span>
    </div>

    

                            </div>
                </section>
                <section id="tabulate">
                            <div class="attr function"><a class="headerlink" href="#tabulate">#&nbsp;&nbsp</a>

        
            <span class="def">def</span>
            <span class="name">tabulate</span><span class="signature">(rows: List[Tuple[str, str]]) -&gt; List[str]</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">def</span> <span class="nf">tabulate</span><span class="p">(</span><span class="n">rows</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
    <span class="n">left_max</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">)</span>
    <span class="n">out</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">left</span><span class="p">,</span> <span class="n">right</span> <span class="ow">in</span> <span class="n">rows</span><span class="p">:</span>
        <span class="n">padding</span> <span class="o">=</span> <span class="p">(</span><span class="n">left_max</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="nb">len</span><span class="p">(</span><span class="n">left</span><span class="p">))</span> <span class="o">*</span> <span class="s2">&quot; &quot;</span>
        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">left</span> <span class="o">+</span> <span class="n">padding</span> <span class="o">+</span> <span class="n">right</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">out</span>
</pre></div>

        </details>

    

                </section>
    </main>
</div>