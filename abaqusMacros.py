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
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup


def Macro1():
    # -*- coding: mbcs -*-
    #
    # Abaqus/CAE Release 2022 replay file
    # Internal Version: 2021_09_16-01.57.30 176069
    # Run by Eric on Wed Aug 23 13:24:27 2023
    #

    # from driverUtils import executeOnCaeGraphicsStartup
    # executeOnCaeGraphicsStartup()
    #: Executing "onCaeGraphicsStartup()" in the site directory ...

    session.Viewport(
        name="Viewport: 1", origin=(0.0, 0.0), width=177.674987792969, height=94.25
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
        name="test", inputFileName="D:/projects/inp_editing/test.inp"
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
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=446.097,
        farPlane=615.411,
        width=462.52,
        height=172.124,
        cameraUpVector=(-0.0826263, 0.996581, 0),
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=335.109,
        farPlane=726.399,
        width=347.446,
        height=129.3,
        cameraPosition=(574.831, -111.574, 53.9986),
        cameraUpVector=(0.296973, 0.816694, 0.494791),
        cameraTarget=(89.9999, 97.5, -0.0999832),
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=408.765,
        farPlane=652.743,
        width=8.079,
        height=3.00656,
        viewOffsetX=7.80307,
        viewOffsetY=-6.7259,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=405.604,
        farPlane=654.34,
        width=8.01653,
        height=2.98331,
        cameraPosition=(552.076, -144.899, 92.6307),
        cameraUpVector=(0.325802, 0.808308, 0.4904),
        cameraTarget=(89.3636, 97.9453, -0.232155),
        viewOffsetX=7.74273,
        viewOffsetY=-6.67389,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=404.915,
        farPlane=655.03,
        width=11.6957,
        height=4.3525,
        viewOffsetX=9.58171,
        viewOffsetY=-6.51434,
    )
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(renderStyle=SHADED)
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(renderStyle=SHADED)
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(renderStyle=SHADED)
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(renderStyle=SHADED)
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(renderStyle=SHADED)
    #:
    #: Element 2231: Linear hexahedron, type C3D8I
    #:    Nodal connectivity: 17841, 17842, 17843, 17844, 17845, 17846, 17847, 17848
    #:
    #: Element 2233: Linear hexahedron, type C3D8I
    #:    Nodal connectivity: 17857, 17858, 17859, 17860, 17861, 17862, 17863, 17864
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=405.032,
        farPlane=654.913,
        width=11.6991,
        height=4.35376,
        cameraPosition=(552.802, -143.587, 92.4443),
        cameraUpVector=(0.360599, 0.841178, 0.402974),
        cameraTarget=(90.0898, 99.2578, -0.418527),
        viewOffsetX=9.58448,
        viewOffsetY=-6.51622,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=405.031,
        farPlane=654.913,
        width=11.6991,
        height=4.35375,
        cameraPosition=(553.6, -142.207, 92.0782),
        cameraUpVector=(0.394206, 0.867324, 0.303894),
        cameraTarget=(90.8875, 100.638, -0.784613),
        viewOffsetX=9.58447,
        viewOffsetY=-6.51621,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=424.956,
        farPlane=618.279,
        width=12.2746,
        height=4.56793,
        cameraPosition=(324.712, -191.264, 365.456),
        cameraUpVector=(0.603537, 0.763896, 0.228487),
        cameraTarget=(88.3582, 106.302, -5.07159),
        viewOffsetX=10.056,
        viewOffsetY=-6.83676,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=424.865,
        farPlane=618.369,
        width=12.272,
        height=4.56695,
        cameraPosition=(318.651, -195.998, 365.52),
        cameraUpVector=(0.194115, 0.821602, 0.535994),
        cameraTarget=(82.2971, 101.568, -5.00716),
        viewOffsetX=10.0538,
        viewOffsetY=-6.83529,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=425.379,
        farPlane=617.854,
        width=8.47633,
        height=3.15442,
        viewOffsetX=11.5756,
        viewOffsetY=-6.48512,
    )
    session.viewports["Viewport: 1"].view.setValues(session.views["Iso"])
    session.viewports["Viewport: 1"].enableMultipleColors()
    session.viewports["Viewport: 1"].setColor(initialColor="#BDBDBD")
    cmap = session.viewports["Viewport: 1"].colorMappings["Material"]
    session.viewports["Viewport: 1"].setColor(colorMapping=cmap)
    session.viewports["Viewport: 1"].disableMultipleColors()
    session.viewports["Viewport: 1"].enableMultipleColors()
    session.viewports["Viewport: 1"].setColor(initialColor="#BDBDBD")
    cmap = session.viewports["Viewport: 1"].colorMappings["Part"]
    session.viewports["Viewport: 1"].setColor(colorMapping=cmap)
    session.viewports["Viewport: 1"].disableMultipleColors()
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=367.304,
        farPlane=721.123,
        width=430.126,
        height=160.069,
        viewOffsetX=-0.817942,
        viewOffsetY=-1.5122,
    )
    del mdb.models["test"]
    a = mdb.models["Model-1"].rootAssembly
    session.viewports["Viewport: 1"].setValues(displayedObject=a)
    mdb.ModelFromInputFile(
        name="test", inputFileName="D:/projects/inp_editing/test.inp"
    )
    #: The model "test" has been created.
    #: The part "PART-1" has been imported from the input file.
    #: The model "test" has been imported from an input file.
    #: Please scroll up to check for error and warning messages.
    a = mdb.models["test"].rootAssembly
    session.viewports["Viewport: 1"].setValues(displayedObject=a)
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=510.233,
        farPlane=517.168,
        width=15.3833,
        height=7.58637,
        viewOffsetX=20.2839,
        viewOffsetY=0.336475,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=450.242,
        farPlane=609.923,
        width=13.5746,
        height=6.6944,
        cameraPosition=(502.564, 149.164, 319.911),
        cameraUpVector=(-0.0793972, 0.995032, -0.0600632),
        cameraTarget=(91.3186, 98.0255, 16.3493),
        viewOffsetX=17.899,
        viewOffsetY=0.296914,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=366.91,
        farPlane=693.255,
        width=393.805,
        height=194.208,
        viewOffsetX=-43.6359,
        viewOffsetY=28.0715,
    )
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
        mask=("[#ffffffff:123 #fffc03ff #ffc03fff #ffffffff:195 #3fffffff ]",),
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
        loads=ON,
        bcs=ON,
        predefinedFields=ON,
        connectors=ON,
        adaptiveMeshConstraints=OFF,
    )
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(
        mesh=ON, loads=OFF, bcs=OFF, predefinedFields=OFF, connectors=OFF
    )
    session.viewports["Viewport: 1"].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON
    )
    session.viewports["Viewport: 1"].assemblyDisplay.setValues(mesh=OFF)
    session.viewports["Viewport: 1"].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF
    )
    mdb.Job(
        name="Job-1",
        model="test",
        description="",
        type=ANALYSIS,
        atTime=None,
        waitMinutes=0,
        waitHours=0,
        queue=None,
        memory=90,
        memoryUnits=PERCENTAGE,
        getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE,
        nodalOutputPrecision=SINGLE,
        echoPrint=OFF,
        modelPrint=OFF,
        contactPrint=OFF,
        historyPrint=OFF,
        userSubroutine="",
        scratch="",
        resultsFormat=ODB,
        numThreadsPerMpiProcess=1,
        multiprocessingMode=DEFAULT,
        numCpus=1,
        numGPUs=0,
    )
    mdb.jobs["Job-1"].submit(consistencyChecking=OFF)
    #: The job input file "Job-1.inp" has been submitted for analysis.
    #: Error in job Job-1: The volume of 10254 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. In the case of a tetrahedron this error may indicate that all nodes are located very nearly in a plane. The elements have been identified in element set ErrElemVolSmallNegZero.
    #: Job Job-1: Analysis Input File Processor aborted due to errors.
    #: Error in job Job-1: Analysis Input File Processor exited with an error - Please see the  Job-1.dat file for possible error messages if the file exists.
    #: Job Job-1 aborted due to errors.
    del mdb.models["test"]
    a = mdb.models["Model-1"].rootAssembly
    session.viewports["Viewport: 1"].setValues(displayedObject=a)
    mdb.ModelFromInputFile(
        name="test", inputFileName="D:/projects/inp_editing/test.inp"
    )
    #: The model "test" has been created.
    #: The part "PART-1" has been imported from the input file.
    #: The model "test" has been imported from an input file.
    #: Please scroll up to check for error and warning messages.
    a = mdb.models["test"].rootAssembly
    session.viewports["Viewport: 1"].setValues(displayedObject=a)
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=500.169,
        farPlane=527.232,
        width=79.969,
        height=31.4446,
        viewOffsetX=-41.9185,
        viewOffsetY=10.3453,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=372.175,
        farPlane=571.445,
        width=59.5048,
        height=23.3979,
        cameraPosition=(541.307, 56.2091, 108.276),
        cameraUpVector=(0.0821535, 0.996612, 0.00392046),
        cameraTarget=(51.5836, 97.1669, -41.3277),
        viewOffsetX=-31.1915,
        viewOffsetY=7.69794,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=378.639,
        farPlane=564.981,
        width=36.9024,
        height=14.5104,
        viewOffsetX=-24.5615,
        viewOffsetY=7.2697,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=379,
        farPlane=564.62,
        width=36.9375,
        height=14.5242,
        cameraPosition=(541.571, 57.8471, 107.86),
        cameraUpVector=(0.0664707, 0.996262, 0.0551618),
        cameraTarget=(51.8476, 98.8049, -41.7434),
        viewOffsetX=-24.5849,
        viewOffsetY=7.27662,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=379,
        farPlane=564.62,
        width=36.9375,
        height=14.5242,
        cameraPosition=(541.487, 57.3092, 107.986),
        cameraUpVector=(0.0716177, 0.996692, 0.0384307),
        cameraTarget=(51.764, 98.267, -41.6169),
        viewOffsetX=-24.5849,
        viewOffsetY=7.27661,
    )
    session.viewports["Viewport: 1"].view.setValues(
        nearPlane=378.999,
        farPlane=564.62,
        width=36.9375,
        height=14.5242,
        cameraPosition=(541.703, 58.7412, 107.671),
        cameraUpVector=(0.057923, 0.994884, 0.0827654),
        cameraTarget=(51.9801, 99.699, -41.9324),
        viewOffsetX=-24.5848,
        viewOffsetY=7.27659,
    )
