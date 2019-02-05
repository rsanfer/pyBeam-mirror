/*
 * pyBeam, a Beam Solver
 *
 * Copyright (C) 2018 Tim Albring, Ruben Sanchez, Rauno Cavallaro
 * 
 * Developers: Tim Albring, Ruben Sanchez (SciComp, TU Kaiserslautern)
 *             Rauno Cavallaro (Carlos III University Madrid)
 *
 * This file is part of pyBeam.
 *
 * pyBeam is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License
 * as published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * pyBeam is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty
 * of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *
 * See the GNU Affero General Public License for more details.
 * You should have received a copy of the GNU Affero
 * General Public License along with pyBeam.
 * If not, see <http://www.gnu.org/licenses/>.
 *
 */


#pragma once
#include <math.h>       /* exp */

#include "../include/types.h"

#include "../include/FiniteElement.h"
#include "../include/StructSyst.h"
#include "../include/geometry.h"
#include "../include/input.h"

class CBeamSolver
{

private:
	
protected:

public:

  CNode **node;                     /*!< \brief Vector which stores the node initial coordinates. */
  CConnectivity **connectivity;      /*!< \brief Vector which stores the connectivity. */

  CInput* input;

  CElement** element;  	  /*!< \brief Vector which the define the elements. */
  
  CStructure* structure;  /*!< \brief Vector which the define the elements. */

  int nDOF, nTotalDOF, nDim;
  addouble *loadVector;
  addouble thickness;

  CBeamSolver(void);
  
  virtual ~CBeamSolver(void);
  
  void Initialize(void);

  void SetLoads(int iNode, int iDOF, passivedouble loadValue);

  void Solve(void);

  passivedouble ExtractDisplacements(int iNode, int iDim);

  passivedouble ExtractCoordinates(int iNode, int iDim);

  passivedouble ExtractInitialCoordinates(int iNode, int iDim);

};
