func assignArgsAndResults(args[]interface{}, results[]interface{})[]interface{} {
    // Define integer and floating-point register sequences and their lengths.
    intRegs := []string{"R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"}
    fpRegs := []string{"F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"}
    numIntRegs := len(intRegs)
    numFpRegs := len(fpRegs)

    // Keep track of the next available integer and floating-point registers.
    i, fp := 0, 0

    // Keep track of the stack frame.
    var stackFrame[]interface{}

    // Assign arguments to registers or the stack.
    for _, arg := range args {
        t := reflect.TypeOf(arg)
        v := reflect.ValueOf(arg)

        // Handle zero-sized arguments.
        if t.Size() == 0 {
            stackFrame = append(stackFrame, arg)
            continue
        }

        // Try to register-assign the argument.
        var assigned bool
        switch t.Kind() {
        case reflect.Bool, reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32:
            if i < numIntRegs {
                fmt.Printf(
                    "Assigned argument %v to integer register %v\n", v, intRegs[i])
                i++
                assigned = true
            }
        case reflect.Int64, reflect.Uint64:
            if i+1 < numIntRegs {
                fmt.Printf(
                    "Assigned argument %v to integer registers %v and %v\n", v, intRegs[i], intRegs[i+1])
                i += 2
                assigned = true
            }
        case reflect.Float32, reflect.Float64:
            if fp < numFpRegs {
                fmt.Printf(
                    "Assigned argument %v to floating-point register %v\n", v, fpRegs[fp])
                fp++
                assigned = true
            }
        case reflect.Complex64, reflect.Complex128:
            realPart := v.FieldByName("real")
            imagPart := v.FieldByName("imag")
            fmt.Printf("Assigning argument %v's real part %v\n", v, realPart)
            assignArgsAndResults([]interface{}{realPart.Interface()}, nil)
            fmt.Printf(
                "Assigning argument %v's imaginary part %v\n", v, imagPart)
            assignArgsAndResults([]interface{}{imagPart.Interface()}, nil)
            assigned = true
        case reflect.Ptr, reflect.Map, reflect.Chan, reflect.Func:
            if i < numIntRegs {
                fmt.Printf(
                    "Assigned argument %v to integer register %v\n", v, intRegs[i])
                i++
                assigned = true
            }
        case reflect.String:
            bytes := v.FieldByName("str")
            len := v.FieldByName("len")
            fmt.Printf("Assigning argument %v's string bytes %v\n", v, bytes)
            assignArgsAndResults([]interface{}{bytes.Interface()}, nil)
            fmt.Printf("Assigning argument %v's string length %v\n", v, len)
            assignArgsAndResults([]interface{}{len.Interface()}, nil)
            assigned = true
        case reflect.Slice:
            ptr := v.FieldByName("ptr")
            len := v.FieldByName("len")
            cap := v.FieldByName("cap")
            fmt.Printf("Assigning argument %







// Assign registers and stack fields for an argument, result, or receiver.
// Returns true if the value was register-assigned.
func assignRegistersAndStackFieldsForValue(T Type, V Value, S * []Type, I * int, FP * int) bool {
    // Remember I and FP.
    origI, origFP := *I, *FP

    // If T has zero size, add T to the stack sequence S and return .
    if T.Size() == 0 {
        *S=append(*S, T)
        return false
    }

    // Try to register-assign V.
    if registerAssignValue(T, V, I, FP) {
        return true
    }

    // Reset I and FP to the values from step 1, add T to the stack sequence S,
    // and assign V to this field in S.
    *I, *FP=origI, origFP
    * S=append(*S, T)
    * S=append(*S, Type{} / * pointer alignment * /)
    * S=append(*S, make([]byte, T.Size()))
    assignValueToField(T, V, (*S)[len(*S)-1])
    return false
}

// Assign registers for a value of base type T.
// Returns true if the value was register-assigned.
func registerAssignValue(T Type, V Value, I * int, FP * int) bool {
    switch T.Kind() {
    case Bool, Int, Uint:
        if T.Size() <= int(RegSize) & & *I < int(NI) {
            assignValueToRegister(T, V, I)
            return true
        }
    case Int8, Uint8, Int16, Uint16, Int32, Uint32:
        if T.Size() <= 4 & & *I < int(NI) {
            assignValueToRegister(T, V, I)
            return true
        }
    case Int64, Uint64:
        if T.Size() <= 8 & & *I < int(NI) {
            assignValueToRegister(T, V, I)
            return true
        } else if T.Size() == 16 & & *FP < int(NFP) {
            assignValueToRegister(T, V, FP)
            * FP++
            return true
        } else if T.Size() > 8 {
            // Handle multi-register integers.
            // ...
        }
    case Float32:
        if T.Size() == 4 & & *FP < int(NFP) {
            assignValueToRegister(T, V, FP)
            * FP++
            return true
        }
    case Float64:
        if T.Size() == 8 & & *FP < int(NFP) {
            assignValueToRegister(T, V, FP)
            * FP++
            return true
        } else if T.Size() == 16 & & *FP+1 < int(NFP) {
            assignValueToRegister(T, V, FP)
            assignValueToRegister(T, V, FP+1)
            * FP += 2
            return true
        }
    case Complex64:
        if *FP+1 < int(NFP) {
            registerAssignValue(T.Elem(), V.Field(0), FP)
            registerAssignValue(T.Elem(), V.Field(1), FP+1)
            * FP += 2
            return true
        }
    case Complex128:
        if *FP+1 < int(NFP) {
            assignValueToRegister(T.Elem(), V.Field(0), FP)
            assignValueToRegister(T





func assignToRegistersOrStack(V Value, T Type, I, FP * int, S * []Type) bool {
    // Step 1: Remember I and FP.
    I0, FP0 := *I, *FP

    // Step 2: If T has zero size, add T to the stack sequence S and return .
    if size(T) == 0 {
        *S=append(*S, T)
        return true
    }

    // Step 3: Try to register-assign V.
    switch {
    case isBool(T) | | isInt(T):
        if I0 < NI {
            assignToReg(V, I0)
            * I=I0 + 1
            return true
        }
    case isInt2(T):
        if I0+1 < NI {
            lo, hi := unpackInt2(V)
            assignToReg(lo, I0)
            assignToReg(hi, I0+1)
            * I=I0 + 2
            return true
        }
    case isFloat(T):
        if FP0 < NFP {
            assignToReg(V, FP0)
            * FP=FP0 + 1
            return true
        }
    case isComplex(T):
        var re, im Value
        if isComplex64(T) {
            re, im=unpackComplex64(V)
        } else {
            re, im=unpackComplex128(V)
        }
        if assignToRegistersOrStack(re, underlyingType(T), I, FP, S) & &
            assignToRegistersOrStack(im, underlyingType(T), I, FP, S) {
            return true
        }
    case isPointer(T) | | isMap(T) | | isChan(T) | | isFunc(T):
        if I0 < NI {
            assignToReg(V, I0)
            * I=I0 + 1
            return true
        }
    case isString(T) | | isSlice(T) | | isInterface(T):
        var ptr, len, cap Value
        if isString(T) {
            ptr, len=unpackString(V)
        } else if isSlice(T) {
            ptr, len, cap=unpackSlice(V)
        } else {
            ptr, cap=unpackInterface(V)
            len=makeInt(len(T))
        }
        if assignToRegistersOrStack(ptr, uintptrType, I, FP, S) & &
            assignToRegistersOrStack(len, intType, I, FP, S) & &
            (cap == nil | | assignToRegistersOrStack(cap, intType, I, FP, S)) {
            return true
        }
    case isStruct(T):
        for i := 0; i < T.NumField(); i++ {
            f := T.Field(i)
            if !assignToRegistersOrStack(V.Field(i), f.Type, I, FP, S) {
                break
            }
        }
        return true
    case isArray(T):
        switch len(T) {
        case 0:
            return true
        case 1:
            return assignToRegistersOrStack(V.Index(0), T.Elem(), I, FP, S)
        default:
            return false
        }
    }

    // Step 4: If step 3 failed, reset I and FP to the values from step 1,
    // add T to the stack sequence S, and assign V to this field in S.
    *I, *FP=I0, FP0
    * S=append(*S, T)
    * S=append(*S, Type{}) // padding
    * S=(*S











// assignRegOrStack assigns a receiver, argument, or result to registers or to a field in the stack sequence.
// The final stack sequence looks like:
// stack-assigned receiver, stack-assigned arguments, pointer-alignment,
// stack-assigned results, pointer-alignment, spill space for each register-assigned argument, pointer-alignment.
func assignRegOrStack(T * types.Type, V * ssa.Value, I * int, FP * int, stk * []*types.Type) {
    if T.Size() == 0 {
        // If T has zero size, add T to the stack sequence S and return .
        *stk=append(*stk, T)
        return
    }
    // Try to register-assign V.
    switch {
    case isBoolOrInt(T):
        if canFitInReg(T, *I) {
            *I++
            break
        }
        if canFitInRegs(T, *I) {
            *I += 2
            break
        }
        fallthrough
    case isFloat(T):
        if canFitInFPReg(T, *FP) {
            *FP++
            break
        }
        fallthrough
    case T.IsComplex():
        r, i := ssa.ComplexComponents(V)
        assignRegOrStack(T.Underlying(), r, I, FP, stk)
        assignRegOrStack(T.Underlying(), i, I, FP, stk)
    case isPointerMapChanFunc(T):
        *I++
    case isStringInterfaceSlice(T):
        for i := 0; i < sliceOrStringSize(T); i++ {
            assignRegOrStack(sliceOrStringElem(
                T), ssa.SliceIndex(V, i), I, FP, stk)
        }
    case T.IsStruct():
        for i := 0; i < T.NumFields(); i++ {
            assignRegOrStack(T.FieldType(i), ssa.Field(V, i), I, FP, stk)
        }
    case T.IsArray():
        if T.NumElem() == 1 {
            assignRegOrStack(T.ElemType(), ssa.Index(
                V, ssa.NewConst(constant.MakeInt64(0))), I, FP, stk)
        } else if T.NumElem() > 1 {
            // Array type of length > 1 can't be register-assigned.
            fallthrough
        }
    default:
        panic(fmt.Sprintf("unknown register-assigned type: %v", T))
    }
    if *I > config.NumIntRegs | | *FP > config.NumFloatRegs {
        panic("too many register-assigned arguments or results")
    }
    if len(*stk) > 0 {
        return
    }
    // Reset I and FP to the values from step 1, add T to the stack sequence S, and assign V to this field in S.
    *I, *FP=0, 0
    * stk=append(*stk, T)
    * stk=append(*stk, nil) // uninitialized spill slot
    ssa.SetSpill(V)
}
