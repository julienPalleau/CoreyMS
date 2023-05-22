function sysCall_init()
    print ("start init ...")
    corout=coroutine.create(coroutineMain)
    print ("... end init")
end

function sysCall_actuation()
    if coroutine.status(corout)~='dead' then
        local ok,errorMsg=coroutine.resume(corout)
        if errorMsg then
            error(debug.traceback(corout,errorMsg),2)
        end
    end
end

function sysCall_sensing()
end 

function sysCall_cleanup()
    print ("start clean up ...")
    print ("handle is "..robHandle)
    print ("Stop ROB1A")
    simRob1A.stop(robHandle)
    print ("ROB1A stopped")
    simRob1A.destroy(robHandle)
    print ("ROB1A destroyed")

    print ("... end clean up")
end

function coroutineMain()
    -- Check if the required plugin is there:
    moduleName=0
    moduleVersion=0
    index=0
    rob1AModuleNotFound=true
    while moduleName do
        moduleName,moduleVersion=sim.getModuleName(index)
        if (moduleName=='Rob1A') then
            rob1AModuleNotFound=false
        end
        index=index+1
    end
    if rob1AModuleNotFound then
        sim.addLog(sim.verbosity_scripterrors,'Rob1A plugin was not found. Simulation will not run properly.')
    else
        print ("Start ROB1A")
        robot=sim.getObject('/Rob1A')
        -- local robotChassisPath='/Rob1A/RobotChassisDyn'
        -- local jointHandles={sim.getObject(robotChassisPath..'/JointWheelLeft'),sim.getObject(robotChassisPath..'/JointWheelRight')}
        -- local sensorHandle=sim.getObject(robotChassisPath..'/RobotCenterMarker/SonarFront/SonarFrontSensor')
        setup_prm_file,do_eval = setup_prms()
        prms = {0.0,0.1,0.2,0.3,0.4}
        if do_eval then
            prms[1] = 1.0
        end
        robHandle=simRob1A.create(robot,setup_prm_file,prms)
        -- robotCollection=sim.createCollection(0)
        -- sim.addItemToCollection(robotCollection,sim.handle_tree,robot,0)
        -- distanceSegment=sim.addDrawingObject(sim.drawing_lines,4,0,-1,1,{0,1,0})
        -- robotTrace=sim.addDrawingObject(sim.drawing_linestrip+sim.drawing_cyclic,2,0,-1,200,{1,1,0},nil,nil,{1,1,0})
        if robHandle>=0 then
            simRob1A.start(robHandle) -- start the robot
            -- sim.wait(300) -- run for 300 seconds
            -- print ("Stop ROB1A")
            -- simRob1A.stop(robHandle)
            -- print ("ROB1A stopped")
            -- simRob1A.destroy(robHandle)
            -- print ("ROB1A destroyed")
        end
    end
end
