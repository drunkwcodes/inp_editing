# -*- coding: mbcs -*-
# Do not delete the following import lines
import __main__
import assembly
import connectorBehavior
import displayGroupMdbToolset as dgm
import displayGroupOdbToolset as dgo
import interaction
import job
import load
import material
import mesh
import optimization
import part
import regionToolset
import section
import sketch
import step
import visualization
import xyPlot
import os
from abaqus import *
from abaqusConstants import *
from caeModules import *


def take_4():
    # -*- coding: mbcs -*-
    #
    # Abaqus/CAE Release 2022 replay file
    # Internal Version: 2021_09_16-01.57.30 176069
    # Run by Eric on Wed Aug 23 16:35:00 2023
    #
    from driverUtils import executeOnCaeStartup

    # from driverUtils import executeOnCaeGraphicsStartup
    # executeOnCaeGraphicsStartup()
    #: Executing "onCaeGraphicsStartup()" in the site directory ...

    session.Viewport(
        name="Viewport: 1",
        origin=(0.0, 0.0),
        width=177.674987792969,
        height=73.9500045776367,
    )
    session.viewports["Viewport: 1"].makeCurrent()
    session.viewports["Viewport: 1"].maximize()
    executeOnCaeStartup()
    session.viewports["Viewport: 1"].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON
    )
    a = mdb.models["Model-1"].rootAssembly
    session.viewports["Viewport: 1"].setValues(displayedObject=a)
    mdb.ModelFromInputFile(
        name="test", inputFileName=os.path.join(os.getcwd(), "test.inp")
    )
    #: The model "test" has been created.
    #: The part "PART-1" has been imported from the input file.
    #: The model "test" has been imported from an input file.
    #: Please scroll up to check for error and warning messages.
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF
    )
    a = mdb.models["test"].rootAssembly
    session.viewports["Viewport: 1"].setValues(displayedObject=a)
    session.viewports["Viewport: 1"].partDisplay.setValues(
        sectionAssignments=ON, engineeringFeatures=ON
    )
    session.viewports["Viewport: 1"].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF
    )
    p = mdb.models["test"].parts["PART-1"]
    session.viewports["Viewport: 1"].setValues(displayedObject=p)
    mdb.models["test"].HomogeneousSolidSection(
        name="Section-1", material="FR4", thickness=None
    )
    p = mdb.models["test"].parts["PART-1"]
    e = p.elements
    elements = e.getSequenceFromMask(
        mask=("[#ffffffff:320 #3fffffff ]",),
    )
    region = p.Set(elements=elements, name="Set-1")
    p = mdb.models["test"].parts["PART-1"]
    p.SectionAssignment(
        region=region,
        sectionName="Section-1",
        offset=0.0,
        offsetType=MIDDLE_SURFACE,
        offsetField="",
        thicknessAssignment=FROM_SECTION,
    )
    a = mdb.models["test"].rootAssembly
    a.regenerate()
    a = mdb.models["test"].rootAssembly
    session.viewports["Viewport: 1"].setValues(displayedObject=a)
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON
    )
    mdb.models["test"].FrequencyStep(
        name="Step-1", previous="Initial", minEigen=1.0, numEigen=10
    )
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(step="Step-1")
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(
        mesh=ON, adaptiveMeshConstraints=OFF
    )
    session.viewports["Viewport: 1"].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON
    )
    p = mdb.models["test"].parts["PART-1"]
    session.viewports["Viewport: 1"].setValues(displayedObject=p)
    session.viewports["Viewport: 1"].partDisplay.setValues(
        sectionAssignments=OFF, engineeringFeatures=OFF, mesh=ON
    )
    session.viewports["Viewport: 1"].partDisplay.meshOptions.setValues(meshTechnique=ON)
    mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
    p = mdb.models["test"].parts["PART-1"]
    e = p.elements
    elements = e.getSequenceFromMask(
        mask=("[#0:123 #3fc00 #3fc000 ]",),
    )
    p.deleteElement(elements=elements, deleteUnreferencedNodes=ON)
