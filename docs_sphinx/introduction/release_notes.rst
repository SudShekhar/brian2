Release notes
=============

Brian 2.0b3
-----------
This is the third beta release for Brian 2.0. This release does not add many new
features but it fixes a number of important bugs so we recommend all users of
Brian 2 to upgrade. If you are a user new to Brian, we also recommend to
directly start with Brian 2 instead of using the stable release of Brian 1.

This is however still a Beta release, please report bugs or suggestions to the
github bug tracker (https://github.com/brian-team/brian2/issues) or to the
brian-development mailing list (brian-development@googlegroups.com).

Major new features
~~~~~~~~~~~~~~~~~~
* A new `PoissonInput` class for efficient simulation of Poisson-distributed
  input events.

Improvements
~~~~~~~~~~~~
* The order of execution for ``pre`` and ``post`` statements happending in the
  same time step was not well defined (it fell back to the default alphabetical
  ordering, executing ``post`` before ``pre``). It now explicitly specifies the
  ``order`` attribute so that ``pre`` gets executed before ``post`` (as in
  Brian 1). See the :doc:`../user/synapses` documentation for details.
* The default schedule that is used can now be set via a preference
  (`core.network.default_schedule`). New automatically generated scheduling
  slots relative to the explicitly defined ones can be used, e.g.
  ``before_resets`` or ``after_synapses``. See :ref:`scheduling` for details.
* The scipy_ package is no longer a dependency (note that weave_ for
  compiled C code under Python 2 is now available in a separate package). Note
  that multicompartmental models will still benefit from the scipy_ package
  if they are simulated in pure Python (i.e. with the ``numpy`` code generation
  target) -- otherwise Brian 2 will fall back to a numpy-only solution which is
  significantly slower.

Important bug fixes
~~~~~~~~~~~~~~~~~~~
* Fix `SpikeGeneratorGroup` which did not emit all the spikes under certain
  conditions for some code generation targets (#429)
* Fix an incorrect update of pre-synaptic variables in synaptic statements for
  the ``numpy`` code generation target (#435).
* Fix the possibility of an incorrect memory access when recording a subgroup
  with `SpikeMonitor` (#454).
* Fix the storing of results on disk for C++ standalone on Windows -- variables
  that had the same name when ignoring case (e.g. ``i`` and ``I``) where
  overwriting each other (#455).

Infrastructure improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Brian 2 now has a chat room on gitter_: https://gitter.im/brian-team/brian2
* The sphinx documentation can now be built from the release archive file
* After a big cleanup, all files in the repository have now simple LF line
  endings (see https://help.github.com/articles/dealing-with-line-endings/ on
  how to configure your own machine properly if you want to contribute to
  Brian).

.. _scipy: http://scipy.org
.. _weave: https://pypi.python.org/pypi/weave
.. _gitter: http://gitter.im

Contributions
~~~~~~~~~~~~~
Code and documentation contributions (ordered by the number of commits):

* Marcel Stimberg (`@mstimberg <https://github.com/mstimberg>`_)
* Dan Goodman (`@thesamovar <https://github.com/thesamovar>`_)
* Konrad Wartke (`@kwartke <https://github.com/Kwartke>`_)

Testing, suggestions and bug reports (ordered alphabetically, apologies to
everyone we forgot...):

* Daniel Bliss
* Owen Mackwood
* Ankur Sinha
* Richard Tomsett


Brian 2.0b2
-----------
This is the second beta release for Brian 2.0, we recommend all users of Brian 2
to upgrade. If you are a user new to Brian, we also recommend to directly start
with Brian 2 instead of using the stable release of Brian 1.

This is however still a Beta release, please report bugs or suggestions to the
github bug tracker (https://github.com/brian-team/brian2/issues) or to the
brian-development mailing list (brian-development@googlegroups.com).

Major new features
~~~~~~~~~~~~~~~~~~
* Multi-compartmental simulations can now be run using the
  :ref:`cpp_standalone` mode (this is not yet well-tested, though).
* The implementation of `TimedArray` now supports two-dimensional arrays, i.e.
  different input per neuron (or synapse, etc.), see :ref:`timed_arrays` for
  details.
* Previously, not setting a code generation target (using the `codegen.target`
  preference) would mean that the ``numpy`` target was used. Now,
  the default target is ``auto``, which means that a compiled language
  (``weave`` or ``cython``) will be used if possible. See
  :doc:`../user/computation` for details.
* The implementation of `SpikeGeneratorGroup` has been improved and it now
  supports a ``period`` argument to repeatedly generate a spike pattern.

Improvements
~~~~~~~~~~~~
* The selection of a numerical algorithm (if none has been specified by the
  user) has been simplified. See :ref:`numerical_integration` for details.
* Expressions that are shared among neurons/synapses are now updated only once
  instead of for every neuron/synapse which can lead to performance
  improvements.
* On Windows, The Microsoft Visual C compiler is now supported in the
  ``cpp_standalone`` mode, see the respective notes in the :doc:`install` and
  :doc:`../user/computation` documents.
* Simulation runs (using the standard "runtime" device) now collect profiling
  information. See :ref:`profiling` for details.

Infrastructure and documentation improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* :doc:`Tutorials for beginners <../resources/tutorials/index>` in the form of
  ipython notebooks (currently only covering the basics of neurons and synapses)
  are now available.
* The :doc:`../examples/index` in the documentation now include the images
  they generated. Several examples have been adapted from Brian 1.
* The code is now automatically tested on Windows machines, using the
  `appveyor <http://ci.appveyor.com>`_ service. This complements the Linux
  testing on `travis <https://travis-ci.org>`_.
* Using a version of a dependency (e.g. sympy) that we don't support will now
  raise an error when you import ``brian2`` -- see :ref:`dependency_checks` for
  more details.
* Test coverage for the ``cpp_standalone`` mode has been significantly
  increased.

Important bug fixes
~~~~~~~~~~~~~~~~~~~
* The preparation time for complicated equations has been significantly reduced.
* The string representation of small physical quantities has been corrected
  (#361)
* Linking variables from a group of size 1 now works correctly (#383)

Contributions
~~~~~~~~~~~~~
Code and documentation contributions (ordered by the number of commits):

* Marcel Stimberg (`@mstimberg <https://github.com/mstimberg>`_)
* Dan Goodman (`@thesamovar <https://github.com/thesamovar>`_)
* Romain Brette (`@romainbrette <https://github.com/romainbrette>`_)
* Pierre Yger (`@yger <https://github.com/yger>`_)

Testing, suggestions and bug reports (ordered alphabetically, apologies to
everyone we forgot...):

* Conor Cox
* Gordon Erlebacher
* Konstantin Mergenthaler


Brian 2.0beta
-------------
This is the first beta release for Brian 2.0 and the first version of Brian 2.0
we recommend for general use. From now on, we will try to keep changes that
break existing code to a minimum. If you are a user new to Brian, we'd
recommend to start with the Brian 2 beta instead of using the stable release of
Brian 1.

This is however still a Beta release, please report bugs or suggestions to the
github bug tracker (https://github.com/brian-team/brian2/issues) or to the
brian-development mailing list (brian-development@googlegroups.com).

Major new features
~~~~~~~~~~~~~~~~~~
* New classes `Morphology` and `SpatialNeuron` for the simulation of
  :doc:`../user/multicompartmental`
* A temporary "bridge" for ``brian.hears`` that allows to use its Brian 1
  version from Brian 2 (:doc:`../user/brian1hears_bridge`)
* Cython is now a new code generation target, therefore the performance benefits
  of compiled code are now also available to users running simulations under
  Python 3.x (where ``scipy.weave`` is not available)
* Networks can now store their current state and return to it at a later time,
  e.g. for simulating multiple trials starting from a fixed network state
  (:ref:`continue_repeat`)
* C++ standalone mode: multiple processors are now supported via OpenMP
  (:ref:`openmp`), although this code has not yet been well tested so may be
  inaccurate.
* C++ standalone mode: after a run, state variables and monitored values can
  be loaded from disk transparently. Most scripts therefore only need two
  additional lines to use standalone mode instead of Brian's default runtime
  mode (:ref:`cpp_standalone`).

Syntax changes
~~~~~~~~~~~~~~
* The syntax and semantics of everything around simulation time steps, clocks,
  and multiple runs have been cleaned up, making ``reinit`` obsolete and also
  making it unnecessary for most users to explicitly generate `Clock` objects --
  instead, a ``dt`` keyword can be specified for objects such as `NeuronGroup`
  (:doc:`../user/running`)
* The ``scalar`` flag for parameters/subexpressions has been renamed to
  ``shared``
* The "unit" for boolean variables has been renamed from ``bool`` to ``boolean``
* C++ standalone: several keywords of
  `CPPStandaloneDevice.build <brian2.devices.cpp_standalone.device.CPPStandaloneDevice.build>`
  have been renamed
* The preferences are now accessible via ``prefs`` instead of ``brian_prefs``
* The ``runner`` method has been renamed to `~brian2.groups.group.Group.custom_operation`

Improvements
~~~~~~~~~~~~
* Variables can now be linked across `NeuronGroup`\ s (:ref:`linked_variables`)
* More flexible progress reporting system, progress reporting also works in the
  C++ standalone mode (:ref:`progress_reporting`)
* State variables can be declared as ``integer`` (:ref:`equation_strings`)

Bug fixes
~~~~~~~~~
57 github issues have been closed since the alpha release, of which 26 had been
labeled as bugs. We recommend all users of Brian 2 to upgrade.

Contributions
~~~~~~~~~~~~~
Code and documentation contributions (ordered by the number of commits):

* Marcel Stimberg (`@mstimberg <https://github.com/mstimberg>`_)
* Dan Goodman (`@thesamovar <https://github.com/thesamovar>`_)
* Romain Brette (`@romainbrette <https://github.com/romainbrette>`_)
* Pierre Yger (`@yger <https://github.com/yger>`_)
* Werner Beroux (`@wernight <https://github.com/wernight>`_)

Testing, suggestions and bug reports (ordered alphabetically, apologies to
everyone we forgot…):

* Guillaume Bellec
* Victor Benichoux
* Laureline Logiaco
* Konstantin Mergenthaler
* Maurizio De Pitta
* Jan-Hendrick Schleimer
* Douglas Sterling
* Katharina Wilmes
