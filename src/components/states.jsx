import React, { Component } from "react";
import { getAll } from "../services/stateService";

class States extends Component {
  state = {
    states: getAll(),
  };
  render() {
    return (
      <div>
        <table className="table">
          <thead>
            <tr>
              <th>Sno.</th>
              <th>State</th>
              <th>Total Cases</th>
              <th>Cured</th>
              <th>Deaths</th>
            </tr>
          </thead>
          <tbody>
            {this.state.states.map((el) => (
              <tr>
                <td>{el.id}</td>
                <td>{el.state}</td>
                <td>{el.Total_Cases}</td>
                <td>{el.Cured}</td>
                <td>{el.Deaths}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default States;
