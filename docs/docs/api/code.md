---
title: reprexlite.code
---
<div>

<style type="text/css">/*! pygments syntax highlighting */pre{line-height:125%;}td.linenos pre{color:#000000; background-color:#f0f0f0; padding-left:5px; padding-right:5px;}span.linenos{color:#000000; background-color:#f0f0f0; padding-left:5px; padding-right:5px;}td.linenos pre.special{color:#000000; background-color:#ffffc0; padding-left:5px; padding-right:5px;}span.linenos.special{color:#000000; background-color:#ffffc0; padding-left:5px; padding-right:5px;}.pdoc .hll{background-color:#ffffcc}.pdoc{background:#f8f8f8;}.pdoc .c{color:#408080; font-style:italic}.pdoc .err{border:1px solid #FF0000}.pdoc .k{color:#008000; font-weight:bold}.pdoc .o{color:#666666}.pdoc .ch{color:#408080; font-style:italic}.pdoc .cm{color:#408080; font-style:italic}.pdoc .cp{color:#BC7A00}.pdoc .cpf{color:#408080; font-style:italic}.pdoc .c1{color:#408080; font-style:italic}.pdoc .cs{color:#408080; font-style:italic}.pdoc .gd{color:#A00000}.pdoc .ge{font-style:italic}.pdoc .gr{color:#FF0000}.pdoc .gh{color:#000080; font-weight:bold}.pdoc .gi{color:#00A000}.pdoc .go{color:#888888}.pdoc .gp{color:#000080; font-weight:bold}.pdoc .gs{font-weight:bold}.pdoc .gu{color:#800080; font-weight:bold}.pdoc .gt{color:#0044DD}.pdoc .kc{color:#008000; font-weight:bold}.pdoc .kd{color:#008000; font-weight:bold}.pdoc .kn{color:#008000; font-weight:bold}.pdoc .kp{color:#008000}.pdoc .kr{color:#008000; font-weight:bold}.pdoc .kt{color:#B00040}.pdoc .m{color:#666666}.pdoc .s{color:#BA2121}.pdoc .na{color:#7D9029}.pdoc .nb{color:#008000}.pdoc .nc{color:#0000FF; font-weight:bold}.pdoc .no{color:#880000}.pdoc .nd{color:#AA22FF}.pdoc .ni{color:#999999; font-weight:bold}.pdoc .ne{color:#D2413A; font-weight:bold}.pdoc .nf{color:#0000FF}.pdoc .nl{color:#A0A000}.pdoc .nn{color:#0000FF; font-weight:bold}.pdoc .nt{color:#008000; font-weight:bold}.pdoc .nv{color:#19177C}.pdoc .ow{color:#AA22FF; font-weight:bold}.pdoc .w{color:#bbbbbb}.pdoc .mb{color:#666666}.pdoc .mf{color:#666666}.pdoc .mh{color:#666666}.pdoc .mi{color:#666666}.pdoc .mo{color:#666666}.pdoc .sa{color:#BA2121}.pdoc .sb{color:#BA2121}.pdoc .sc{color:#BA2121}.pdoc .dl{color:#BA2121}.pdoc .sd{color:#BA2121; font-style:italic}.pdoc .s2{color:#BA2121}.pdoc .se{color:#BB6622; font-weight:bold}.pdoc .sh{color:#BA2121}.pdoc .si{color:#BB6688; font-weight:bold}.pdoc .sx{color:#008000}.pdoc .sr{color:#BB6688}.pdoc .s1{color:#BA2121}.pdoc .ss{color:#19177C}.pdoc .bp{color:#008000}.pdoc .fm{color:#0000FF}.pdoc .vc{color:#19177C}.pdoc .vg{color:#19177C}.pdoc .vi{color:#19177C}.pdoc .vm{color:#19177C}.pdoc .il{color:#666666}</style>
<style type="text/css">/*! pdoc */:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f7f7f7;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}html, main{scroll-behavior:smooth;}.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3, .pdoc h4{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{background-color:var(--code);border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--code);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.pdoc details{--shift:-40px;text-align:right;margin-top:var(--shift);margin-bottom:calc(0px - var(--shift));clear:both;filter:opacity(1);}.pdoc details:not([open]){height:0;overflow:visible;}.pdoc details > summary{font-size:.75rem;cursor:pointer;color:var(--muted);border-width:0;padding:0 .7em;display:inline-block;display:inline list-item;user-select:none;}.pdoc details > summary:focus{outline:0;}.pdoc details > div{margin-top:calc(0px - var(--shift) / 2);text-align:left;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc > section:first-of-type > .docstring{margin-bottom:3rem;}.pdoc .docstring pre{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc .headerlink{position:absolute;width:0;margin-left:-1.5rem;line-height:1.4rem;font-size:1.5rem;font-weight:normal;transition:all 100ms ease-in-out;opacity:0;}.pdoc .attr > .headerlink{margin-left:-2.5rem;}.pdoc *:hover > .headerlink,.pdoc *:target > .attr > .headerlink{opacity:1;}.pdoc .attr{color:var(--text);margin:1rem 0 .5rem;padding:.4rem 5rem .4rem 1rem;background-color:var(--accent);}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{white-space:pre-wrap;}.pdoc .annotation{color:var(--annotation);}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}</style>    <main class="pdoc">
            <section>
                    <h1 class="modulename">
reprexlite.code    </h1>

                
                        <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">chain</span>
<span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pformat</span>
<span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Union</span>

<span class="kn">import</span> <span class="nn">libcst</span> <span class="k">as</span> <span class="nn">cst</span>


<span class="n">NO_RETURN</span> <span class="o">=</span> <span class="nb">object</span><span class="p">()</span>
<span class="sd">&quot;&quot;&quot;Explicit placeholder object for statements, which have no return value (as opposed to</span>
<span class="sd">expressions).&quot;&quot;&quot;</span>


<span class="k">class</span> <span class="nc">Result</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class that holds the result of evaluated code. Use `str(...)` on an instance to produce a</span>
<span class="sd">    pretty-formatted comment block representation of the result.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        result (Any): Some Python object, intended to be the return value of evaluated Python code.</span>
<span class="sd">        comment (str): Line prefix to use when rendering the result for a reprex.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">comment</span> <span class="o">=</span> <span class="n">comment</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">&quot;&quot;</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">result</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">77</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">comment</span><span class="si">}</span><span class="s2"> &quot;</span> <span class="o">+</span> <span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">NO_RETURN</span>


<span class="k">class</span> <span class="nc">Statement</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class that holds a LibCST parsed statement. The evaluate method will evaluate the statement</span>
<span class="sd">    and return a [`Result`][reprexlite.code.Result] object. To recover the original source code</span>
<span class="sd">    for an instancement, call `str(...)` on it. You can optionally autoformat the returned source</span>
<span class="sd">    code, controlled by the `style` attribute.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed</span>
<span class="sd">            statement.</span>
<span class="sd">        style (bool): Whether to autoformat the source code with black.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">stmt</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cst</span><span class="o">.</span><span class="n">SimpleStatementLine</span><span class="p">,</span> <span class="n">cst</span><span class="o">.</span><span class="n">BaseCompoundStatement</span><span class="p">],</span> <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">stmt</span> <span class="o">=</span> <span class="n">stmt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">style</span> <span class="o">=</span> <span class="n">style</span>

    <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scope</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Result</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Result</span><span class="p">(</span><span class="nb">eval</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">scope</span><span class="p">,</span> <span class="n">scope</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">SyntaxError</span><span class="p">:</span>
            <span class="n">exec</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">scope</span><span class="p">,</span> <span class="n">scope</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">Result</span><span class="p">(</span><span class="n">NO_RETURN</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">code</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">stmt</span><span class="p">])</span><span class="o">.</span><span class="n">code</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">style</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">black</span> <span class="kn">import</span> <span class="n">format_str</span><span class="p">,</span> <span class="n">Mode</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">&quot;Must install black to restyle code.&quot;</span><span class="p">)</span>

            <span class="n">code</span> <span class="o">=</span> <span class="n">format_str</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">Mode</span><span class="p">())</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">code</span>


<span class="k">class</span> <span class="nc">CodeBlock</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class that takes a block of Python code input and evaluates it. Call `str(...)` on an</span>
<span class="sd">    instance to get back a string containing the original source with evaluated outputs embedded</span>
<span class="sd">    as comments below each statement.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        input (str): Block of Python code</span>
<span class="sd">        style (bool): Whether to use black to autoformat code in returned string representation.</span>
<span class="sd">        comment (str): Line prefix to use when rendering the evaluated results.</span>
<span class="sd">        terminal (bool): Whether to apply syntax highlighting to the string representation.</span>
<span class="sd">            Requires optional dependency Pygments.</span>
<span class="sd">        tree (libcst.Module): Parsed LibCST concrete syntax tree of input code.</span>
<span class="sd">        statements (List[Statement]): List of individual statements parsed from input code.</span>
<span class="sd">        results (List[Result]): List of evaluated results corresponding to each item of statements.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">,</span> <span class="n">terminal</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">input</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">input</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">terminal</span> <span class="o">=</span> <span class="n">terminal</span>
        <span class="c1"># Parse code</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">:</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">parse_module</span><span class="p">(</span><span class="nb">input</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Statement</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">Statement</span><span class="p">(</span><span class="n">stmt</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">style</span><span class="p">)</span> <span class="k">for</span> <span class="n">stmt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">body</span>
        <span class="p">]</span>
        <span class="c1"># Evaluate code</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Result</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">stmt</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">)</span> <span class="k">for</span> <span class="n">stmt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">res</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span>
            <span class="n">res</span><span class="o">.</span><span class="n">comment</span> <span class="o">=</span> <span class="n">comment</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">header</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="p">[],</span> <span class="n">header</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">header</span><span class="p">)</span><span class="o">.</span><span class="n">code</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="n">code</span> <span class="o">=</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">chain</span><span class="o">.</span><span class="n">from_iterable</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">))</span> <span class="k">if</span> <span class="n">line</span>
        <span class="p">)</span>
        <span class="n">footer</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="p">[],</span> <span class="n">footer</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">footer</span><span class="p">)</span><span class="o">.</span><span class="n">code</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="n">out</span> <span class="o">=</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">header</span><span class="p">,</span> <span class="n">code</span><span class="p">,</span> <span class="n">footer</span><span class="p">])</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">terminal</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">pygments</span> <span class="kn">import</span> <span class="n">highlight</span>
                <span class="kn">from</span> <span class="nn">pygments.lexers</span> <span class="kn">import</span> <span class="n">PythonLexer</span>
                <span class="kn">from</span> <span class="nn">pygments.formatters</span> <span class="kn">import</span> <span class="n">Terminal256Formatter</span>

                <span class="n">out</span> <span class="o">=</span> <span class="n">highlight</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">PythonLexer</span><span class="p">(),</span> <span class="n">Terminal256Formatter</span><span class="p">())</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">pass</span>
        <span class="k">return</span> <span class="n">out</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_repr_html_</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
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
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>
</pre></div>

        </details>

            </section>
                <section id="NO_RETURN">
                                <div class="attr variable"><a class="headerlink" href="#NO_RETURN">#&nbsp;&nbsp</a>

        <span class="name">NO_RETURN</span><span class="default_value"> = &lt;object object&gt;</span>
    </div>

            <div class="docstring"><p>Explicit placeholder object for statements, which have no return value (as opposed to
expressions).</p>
</div>


                </section>
                <section id="Result">
                                <div class="attr class">
        <a class="headerlink" href="#Result">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">Result</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Result</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class that holds the result of evaluated code. Use `str(...)` on an instance to produce a</span>
<span class="sd">    pretty-formatted comment block representation of the result.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        result (Any): Some Python object, intended to be the return value of evaluated Python code.</span>
<span class="sd">        comment (str): Line prefix to use when rendering the result for a reprex.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">comment</span> <span class="o">=</span> <span class="n">comment</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="p">:</span>
            <span class="k">return</span> <span class="s2">&quot;&quot;</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">result</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">77</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">comment</span><span class="si">}</span><span class="s2"> &quot;</span> <span class="o">+</span> <span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">NO_RETURN</span>
</pre></div>

        </details>

            <div class="docstring"><p>Class that holds the result of evaluated code. Use <code>str(...)</code> on an instance to produce a
pretty-formatted comment block representation of the result.</p>

<p>Attributes:
    result (Any): Some Python object, intended to be the return value of evaluated Python code.
    comment (str): Line prefix to use when rendering the result for a reprex.</p>
</div>


                            <div id="Result.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Result.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">Result</span><span class="signature">(result: Any, comment: str = &#39;#&gt;&#39;)</span>    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">comment</span> <span class="o">=</span> <span class="n">comment</span>
</pre></div>

        </details>

    

                            </div>
                </section>
                <section id="Statement">
                                <div class="attr class">
        <a class="headerlink" href="#Statement">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">Statement</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Statement</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class that holds a LibCST parsed statement. The evaluate method will evaluate the statement</span>
<span class="sd">    and return a [`Result`][reprexlite.code.Result] object. To recover the original source code</span>
<span class="sd">    for an instancement, call `str(...)` on it. You can optionally autoformat the returned source</span>
<span class="sd">    code, controlled by the `style` attribute.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed</span>
<span class="sd">            statement.</span>
<span class="sd">        style (bool): Whether to autoformat the source code with black.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">stmt</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cst</span><span class="o">.</span><span class="n">SimpleStatementLine</span><span class="p">,</span> <span class="n">cst</span><span class="o">.</span><span class="n">BaseCompoundStatement</span><span class="p">],</span> <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">stmt</span> <span class="o">=</span> <span class="n">stmt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">style</span> <span class="o">=</span> <span class="n">style</span>

    <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scope</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Result</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Result</span><span class="p">(</span><span class="nb">eval</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">scope</span><span class="p">,</span> <span class="n">scope</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">SyntaxError</span><span class="p">:</span>
            <span class="n">exec</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">scope</span><span class="p">,</span> <span class="n">scope</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">Result</span><span class="p">(</span><span class="n">NO_RETURN</span><span class="p">)</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">code</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">stmt</span><span class="p">])</span><span class="o">.</span><span class="n">code</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">style</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">black</span> <span class="kn">import</span> <span class="n">format_str</span><span class="p">,</span> <span class="n">Mode</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">&quot;Must install black to restyle code.&quot;</span><span class="p">)</span>

            <span class="n">code</span> <span class="o">=</span> <span class="n">format_str</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="n">Mode</span><span class="p">())</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">code</span>
</pre></div>

        </details>

            <div class="docstring"><p>Class that holds a LibCST parsed statement. The evaluate method will evaluate the statement
and return a [<code><a href="#Result">Result</a></code>][<a href="#Result">reprexlite.code.Result</a>] object. To recover the original source code
for an instancement, call <code>str(...)</code> on it. You can optionally autoformat the returned source
code, controlled by the <code>style</code> attribute.</p>

<p>Attributes:
    stmt (Union[libcst.SimpleStatementLine, libcst.BaseCompoundStatement]): LibCST parsed
        statement.
    style (bool): Whether to autoformat the source code with black.</p>
</div>


                            <div id="Statement.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Statement.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">Statement</span><span class="signature">(
    self,
    stmt: Union[libcst._nodes.statement.SimpleStatementLine, libcst._nodes.statement.BaseCompoundStatement],
    style: bool = False
)</span>    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">stmt</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cst</span><span class="o">.</span><span class="n">SimpleStatementLine</span><span class="p">,</span> <span class="n">cst</span><span class="o">.</span><span class="n">BaseCompoundStatement</span><span class="p">],</span> <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">stmt</span> <span class="o">=</span> <span class="n">stmt</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">style</span> <span class="o">=</span> <span class="n">style</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="Statement.evaluate" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#Statement.evaluate">#&nbsp;&nbsp</a>

        
            <span class="def">def</span>
            <span class="name">evaluate</span><span class="signature">(self, scope: dict) -&gt; <a href="#Result">reprexlite.code.Result</a></span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scope</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Result</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Result</span><span class="p">(</span><span class="nb">eval</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">scope</span><span class="p">,</span> <span class="n">scope</span><span class="p">))</span>
        <span class="k">except</span> <span class="ne">SyntaxError</span><span class="p">:</span>
            <span class="n">exec</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">scope</span><span class="p">,</span> <span class="n">scope</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">Result</span><span class="p">(</span><span class="n">NO_RETURN</span><span class="p">)</span>
</pre></div>

        </details>

    

                            </div>
                </section>
                <section id="CodeBlock">
                                <div class="attr class">
        <a class="headerlink" href="#CodeBlock">#&nbsp;&nbsp</a>

        
        <span class="def">class</span>
        <span class="name">CodeBlock</span>:
    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">CodeBlock</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Class that takes a block of Python code input and evaluates it. Call `str(...)` on an</span>
<span class="sd">    instance to get back a string containing the original source with evaluated outputs embedded</span>
<span class="sd">    as comments below each statement.</span>

<span class="sd">    Attributes:</span>
<span class="sd">        input (str): Block of Python code</span>
<span class="sd">        style (bool): Whether to use black to autoformat code in returned string representation.</span>
<span class="sd">        comment (str): Line prefix to use when rendering the evaluated results.</span>
<span class="sd">        terminal (bool): Whether to apply syntax highlighting to the string representation.</span>
<span class="sd">            Requires optional dependency Pygments.</span>
<span class="sd">        tree (libcst.Module): Parsed LibCST concrete syntax tree of input code.</span>
<span class="sd">        statements (List[Statement]): List of individual statements parsed from input code.</span>
<span class="sd">        results (List[Result]): List of evaluated results corresponding to each item of statements.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">,</span> <span class="n">terminal</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">input</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">input</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">terminal</span> <span class="o">=</span> <span class="n">terminal</span>
        <span class="c1"># Parse code</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">:</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">parse_module</span><span class="p">(</span><span class="nb">input</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Statement</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">Statement</span><span class="p">(</span><span class="n">stmt</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">style</span><span class="p">)</span> <span class="k">for</span> <span class="n">stmt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">body</span>
        <span class="p">]</span>
        <span class="c1"># Evaluate code</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Result</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">stmt</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">)</span> <span class="k">for</span> <span class="n">stmt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">res</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span>
            <span class="n">res</span><span class="o">.</span><span class="n">comment</span> <span class="o">=</span> <span class="n">comment</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">header</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="p">[],</span> <span class="n">header</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">header</span><span class="p">)</span><span class="o">.</span><span class="n">code</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="n">code</span> <span class="o">=</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="nb">str</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">chain</span><span class="o">.</span><span class="n">from_iterable</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">))</span> <span class="k">if</span> <span class="n">line</span>
        <span class="p">)</span>
        <span class="n">footer</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span><span class="p">(</span><span class="n">body</span><span class="o">=</span><span class="p">[],</span> <span class="n">footer</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">footer</span><span class="p">)</span><span class="o">.</span><span class="n">code</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="n">out</span> <span class="o">=</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">header</span><span class="p">,</span> <span class="n">code</span><span class="p">,</span> <span class="n">footer</span><span class="p">])</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">terminal</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">pygments</span> <span class="kn">import</span> <span class="n">highlight</span>
                <span class="kn">from</span> <span class="nn">pygments.lexers</span> <span class="kn">import</span> <span class="n">PythonLexer</span>
                <span class="kn">from</span> <span class="nn">pygments.formatters</span> <span class="kn">import</span> <span class="n">Terminal256Formatter</span>

                <span class="n">out</span> <span class="o">=</span> <span class="n">highlight</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">PythonLexer</span><span class="p">(),</span> <span class="n">Terminal256Formatter</span><span class="p">())</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">pass</span>
        <span class="k">return</span> <span class="n">out</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">_repr_html_</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
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
        <span class="k">return</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span>
</pre></div>

        </details>

            <div class="docstring"><p>Class that takes a block of Python code input and evaluates it. Call <code>str(...)</code> on an
instance to get back a string containing the original source with evaluated outputs embedded
as comments below each statement.</p>

<p>Attributes:
    input (str): Block of Python code
    style (bool): Whether to use black to autoformat code in returned string representation.
    comment (str): Line prefix to use when rendering the evaluated results.
    terminal (bool): Whether to apply syntax highlighting to the string representation.
        Requires optional dependency Pygments.
    tree (libcst.Module): Parsed LibCST concrete syntax tree of input code.
    statements (List[Statement]): List of individual statements parsed from input code.
    results (List[Result]): List of evaluated results corresponding to each item of statements.</p>
</div>


                            <div id="CodeBlock.__init__" class="classattr">
                                        <div class="attr function"><a class="headerlink" href="#CodeBlock.__init__">#&nbsp;&nbsp</a>

        
            <span class="name">CodeBlock</span><span class="signature">(
    self,
    input: str,
    style: bool = False,
    comment: str = &#39;#&gt;&#39;,
    terminal=False
)</span>    </div>

                <details>
            <summary>View Source</summary>
            <div class="codehilite"><pre><span></span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">style</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">comment</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">&quot;#&gt;&quot;</span><span class="p">,</span> <span class="n">terminal</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">input</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">input</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">terminal</span> <span class="o">=</span> <span class="n">terminal</span>
        <span class="c1"># Parse code</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">:</span> <span class="n">cst</span><span class="o">.</span><span class="n">Module</span> <span class="o">=</span> <span class="n">cst</span><span class="o">.</span><span class="n">parse_module</span><span class="p">(</span><span class="nb">input</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Statement</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">Statement</span><span class="p">(</span><span class="n">stmt</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">style</span><span class="p">)</span> <span class="k">for</span> <span class="n">stmt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">body</span>
        <span class="p">]</span>
        <span class="c1"># Evaluate code</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Result</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">stmt</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">)</span> <span class="k">for</span> <span class="n">stmt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">statements</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">res</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span>
            <span class="n">res</span><span class="o">.</span><span class="n">comment</span> <span class="o">=</span> <span class="n">comment</span>
</pre></div>

        </details>

    

                            </div>
                            <div id="CodeBlock.input" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#CodeBlock.input">#&nbsp;&nbsp</a>

        <span class="name">input</span><span class="annotation">: str</span>
    </div>

    

                            </div>
                            <div id="CodeBlock.tree" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#CodeBlock.tree">#&nbsp;&nbsp</a>

        <span class="name">tree</span><span class="annotation">: libcst._nodes.module.Module</span>
    </div>

    

                            </div>
                            <div id="CodeBlock.statements" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#CodeBlock.statements">#&nbsp;&nbsp</a>

        <span class="name">statements</span><span class="annotation">: List[<a href="#Statement">reprexlite.code.Statement</a>]</span>
    </div>

    

                            </div>
                            <div id="CodeBlock.namespace" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#CodeBlock.namespace">#&nbsp;&nbsp</a>

        <span class="name">namespace</span><span class="annotation">: dict</span>
    </div>

    

                            </div>
                            <div id="CodeBlock.results" class="classattr">
                                            <div class="attr variable"><a class="headerlink" href="#CodeBlock.results">#&nbsp;&nbsp</a>

        <span class="name">results</span><span class="annotation">: List[<a href="#Result">reprexlite.code.Result</a>]</span>
    </div>

    

                            </div>
                </section>
    </main>
</div>